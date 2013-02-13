// SkypePlugin.cpp : Defines the entry point for the DLL application.
//

#include "stdafx.h"

#import "C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\mscorlib.tlb" no_namespace named_guids rename("ReportEvent", "_ReportEvent")

#ifdef _DEBUG
	#import "..\..\bin\Debug\Adviser\WindowFinderNET.tlb" no_namespace
	#import "..\..\bin\Debug\Adviser\SkypeHandlerNET.tlb" no_namespace rename("SendMessage", "_SendMessage")
#else
	#import "..\..\bin\Release\Adviser\WindowFinderNET.tlb" no_namespace
	#import "..\..\bin\Release\Adviser\SkypeHandlerNET.tlb" no_namespace rename("SendMessage", "_SendMessage")
#endif

#define DO_INTERNAL(command, arg) _variant_t varIn(command); _variant_t varOut(arg); g_spHandlerNET->Do(varIn, &varOut);
#define DO(command, arg) { DO_INTERNAL(command, arg) }
#define DO_WITH_OUTPUT(command, arg, output, val) { DO_INTERNAL(command, arg) output = varOut.val; }

LPCTSTR g_szTargetWndClass = _T("TLiveConversationWindow");

const UINT WM_CREATE_OBJECT = RegisterWindowMessage(_T("Create Object"));

const UINT TIMER_INTERVAL = 5 * 1000;
const UINT POINT_PROXIMITY = 5;

static DWORD g_pfnOldFrameWndProc;	      // pointer to original frame window procedure
static DWORD g_pfnOldViewWndProc;         // pointer to original view  window procedure

static IHandlerPtr g_spHandlerNET = NULL; // pointer to embedded COM object
static HWND g_hFrameWnd = 0;

static _bstr_t bstCaption;

static long xDown, yDown, xOrg, yOrg;
static int orgCorner = 0;

static bool g_bDragPicture = false;
static UINT timerId = 0;
static _bstr_t bstText(_T(""));

void TransferPositionCommand(TCHAR* szCommand, long x, long y)
{
	if (NULL != g_spHandlerNET)
	{
		SetCursor(LoadCursor(0, IDC_ARROW));

		_bstr_t bsCommand(szCommand);
		_bstr_t bsCommandX = bsCommand + _bstr_t(_T("X"));
		_bstr_t bsCommandY = bsCommand + _bstr_t(_T("Y"));

		// Two calls to define point
		DO(bsCommandX, x + xOrg)
		DO(bsCommandY, y + yOrg)
	}
}

void TransferPositionCommand(TCHAR* szCommand, LPARAM lParam)
{
	TransferPositionCommand(szCommand, LOWORD(lParam), HIWORD(lParam));
}

bool IsClick(long dx, long dy)
{
	return abs(dx) < POINT_PROXIMITY && abs(dy) < POINT_PROXIMITY;
}

//
// New view window procedure
//
LRESULT CALLBACK ViewWndProc(HWND hWnd, UINT dwMsg, WPARAM wParam, LPARAM lParam) 
{
	switch (dwMsg)
	{
	case WM_MOUSEMOVE:
		if (wParam & MK_SHIFT)
			break;
		else 
		{
			SetCursor(LoadCursor(0, IDC_ARROW));
			return 0;
		}

	case WM_LBUTTONDOWN:
		xDown = LOWORD(lParam);
		yDown = HIWORD(lParam);		
		if (wParam & MK_SHIFT)
		{			
			g_bDragPicture = true;
			break;
		}
		else 
		{
			SetCursor(LoadCursor(0, IDC_ARROW));
			return 0;
		}

	case WM_RBUTTONDOWN:
		xDown = LOWORD(lParam);
		yDown = HIWORD(lParam);		
		SetCursor(LoadCursor(0, IDC_ARROW));
		return 0;

	case WM_LBUTTONUP:
		{
		long xUp = LOWORD(lParam);
		long yUp = HIWORD(lParam);
		long dx = xUp - xDown;
		long dy = yUp - yDown;

		if (!g_bDragPicture)
		{
			SetCursor(LoadCursor(0, IDC_ARROW));

			if (IsClick(dx, dy))
				// Left click
				TransferPositionCommand(_T("LClick"), xUp, yUp);
			else
			{
				// Move pressed left mouse button
				TransferPositionCommand(_T("PressedMoveFrom"), xDown, yDown);
				TransferPositionCommand(_T("PressedMoveTo"), xUp, yUp);
			}
			return 0;
		}
		else
		{
			g_bDragPicture = false;

			// Drag entire picture
			orgCorner = dy < 0 ? 1 : 0;
			
			DO_WITH_OUTPUT(_T("GetOffsetX"), orgCorner, xOrg, lVal)
			DO_WITH_OUTPUT(_T("GetOffsetY"), orgCorner, yOrg, lVal)
		}
		}
		break;

	case WM_RBUTTONUP:
		SetCursor(LoadCursor(0, IDC_ARROW));
		TransferPositionCommand(_T("RClick"), lParam);
		return 0;

	case WM_CHAR:
		// Key pressed, char inserted to view window
		if (NULL != g_spHandlerNET)
		{
			TCHAR szChar[2];
			_stprintf(szChar, _T("%c"), (TCHAR)wParam);

			// Pass inserted character on to embedded .NET object wrapped in COM
			_bstr_t bs(szChar);
			bstText += bs;
		}
		
	case WM_KEYDOWN:
	case WM_KEYUP:
		if (wParam == VK_SPACE || wParam == VK_RETURN || wParam == VK_TAB)
			return 0;
		break;

	case WM_TIMER:
		if (bstText.length() > 0)
		{
			DO(_T("Text"), bstText)
			bstText = _bstr_t(_T(""));
		}
		break;
	}

	// Pass message on to the original window procedure
	return CallWindowProc((WNDPROC)g_pfnOldViewWndProc, hWnd, dwMsg, wParam, lParam);
}

//
// New frame window procedure
//
LRESULT CALLBACK FrameWndProc(HWND hWnd, UINT dwMsg, WPARAM wParam, LPARAM lParam) 
{
	HRESULT hr = E_FAIL;

	if (WM_CREATE_OBJECT == dwMsg)
	{
		// Handler of special message to create embedded COM object
		if (FAILED(CoInitialize(NULL)))
		{
			// If COM initialization failed then restore original window procedure
			SetWindowLong(hWnd, GWL_WNDPROC, (DWORD)g_pfnOldFrameWndProc);
			return 0;
		}	

		if (NULL == g_spHandlerNET)
			// Create embedded COM object. This is a COM-wrapped managed SkypeHandleNET object.
			hr = g_spHandlerNET.CreateInstance(__uuidof(Handler));

		g_hFrameWnd = hWnd;

		if (SUCCEEDED(hr))
		{		
			// Change caption of the frame window by sending (posting - ?) WM_SETTEXT
			TCHAR szCaption[MAX_PATH];
			GetWindowText(hWnd, szCaption, MAX_PATH);
			SetWindowText(hWnd, szCaption);

			DO(_T("hWndFrame"), (long)hWnd)
			DO(_T("hWndView"), (long)GetWindow(hWnd, GW_CHILD))
			DO(_T("ResizeOperativeWindow"), 0)
		
			timerId = SetTimer(GetWindow(hWnd, GW_CHILD), 0, TIMER_INTERVAL, NULL);
		}

		return hr;
	}

	switch (dwMsg)
	{
	case WM_SHOWWINDOW:
		if ((BOOL)wParam)
		{
			// Subclass view window
			g_pfnOldViewWndProc = SetWindowLong(GetWindow(hWnd, GW_CHILD), GWL_WNDPROC, (DWORD)ViewWndProc);

			// Change caption of the frame window by sending (posting - ?) WM_SETTEXT
			TCHAR szCaption[MAX_PATH];
			GetWindowText(hWnd, szCaption, MAX_PATH);
			SetWindowText(hWnd, szCaption);

			KillTimer(GetWindow(hWnd, GW_CHILD), 0);
			timerId = SetTimer(GetWindow(hWnd, GW_CHILD), 0, TIMER_INTERVAL, NULL);
		}
		break;

	case WM_DESTROY:
		if (NULL != g_spHandlerNET)
		{
			KillTimer(GetWindow(hWnd, GW_CHILD), 0);

			DO(_T("Destroy"), 0)
		}

		g_spHandlerNET = NULL;
		MessageBox(hWnd, _T("Collaboration windows was destroyed.\nThank you for using SkypeGuide"), _T("Skype"), MB_TOPMOST);
		break;

	case WM_SETTEXT:
		bstCaption = _bstr_t((LPSTR)lParam) + _bstr_t(_T(" (AUTOMATED)"));
		lParam = (LPARAM)(LPCTSTR)bstCaption;
		break;
	}

	// Pass message on to the original window procedure
	return CallWindowProc((WNDPROC)g_pfnOldFrameWndProc, hWnd, dwMsg, wParam, lParam);
}

//
// Injected DLL activities function
//
BOOL PluginProc()
{
	if (FAILED(CoInitialize(NULL)))
		return FALSE;

	IWndFinderPtr spWndFinder(__uuidof(WndFinder));
	if (NULL == spWndFinder)
		return FALSE;

	// Find/wait for window of specified class
	ULONG lWnd = spWndFinder->GetWindow(g_szTargetWndClass);
	if (0 >= lWnd)
		return FALSE;

	HWND hWnd = (HWND)lWnd;

	// Subclass frame window of target application
	g_pfnOldFrameWndProc = SetWindowLong(hWnd, GWL_WNDPROC, (DWORD)FrameWndProc);

	// Subclass view window
	g_pfnOldViewWndProc = SetWindowLong(GetWindow(hWnd, GW_CHILD), GWL_WNDPROC, (DWORD)ViewWndProc);

	// Post message to new window procedure to create COM object
	PostMessage(hWnd, WM_CREATE_OBJECT, 0, 0);

	return TRUE;
}
	
//
// Dll entry point
//
BOOL WINAPI DllMain(HINSTANCE hInstance, DWORD nReason, LPVOID pReserved)
{
	BOOL br = FALSE;
	if (nReason == DLL_PROCESS_ATTACH)
		br = PluginProc();

	return br;
}
