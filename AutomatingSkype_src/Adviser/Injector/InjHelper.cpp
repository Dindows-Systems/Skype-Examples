// InjHelper.cpp : Implementation of CInjHelper

#include "stdafx.h"
#include "InjHelper.h"

#import "C:\WINDOWS\Microsoft.NET\Framework\v2.0.50727\mscorlib.tlb" no_namespace named_guids rename("ReportEvent", "_ReportEvent")

#ifdef _DEBUG
	#import "..\..\bin\Debug\Adviser\WindowFinderNET.tlb" no_namespace
#else
	#import "..\..\bin\Release\Adviser\WindowFinderNET.tlb" no_namespace
#endif

LPCTSTR g_szKernel = _T("Kernel32.dll");
const char g_szLoadLibrary[] = "LoadLibraryA";

//
// Get process handle by name	
//
HANDLE GetProcessHandle(LPCTSTR szProcessName)
{
	const DWORD dwSize = 512;
	DWORD dwProcessID[dwSize];
	DWORD dwNeeded;
	HANDLE hProcess = NULL;

	// Get the list of process identifiers
	if (!EnumProcesses(dwProcessID, dwSize, &dwNeeded))
		return NULL;
	
	// Calculate how many process identifiers were returned
	DWORD dwProcessesNum = dwNeeded / sizeof(DWORD);
	
	// Find handle of required process
	for (DWORD i=0; i<dwProcessesNum; i++)
	{
		hProcess = OpenProcess(PROCESS_ALL_ACCESS, FALSE, dwProcessID[i]);	
		if (0 != hProcess)
		{
			HMODULE hMod;			
			if (EnumProcessModules(hProcess, &hMod, sizeof(hMod), &dwNeeded))
			{
				TCHAR szCurProcessName[dwSize];
				GetModuleBaseName(hProcess, hMod, szCurProcessName, sizeof(szCurProcessName));
				if (!_tcsicmp(szCurProcessName, szProcessName))
					return hProcess;
			}
		}
		
		CloseHandle(hProcess);
	}

	return NULL;
}

// CInjHelper

//
// Inject DLL to target process. If target process is not running then start it.
//
STDMETHODIMP CInjHelper::Run(BSTR bsTargetPath, BSTR bsPluginPath, BSTR bsTargetWndClass)
{
	HRESULT  hr = S_OK;
	_bstr_t bstTargetPath(bsTargetPath);
	_bstr_t bstPluginPath(bsPluginPath);
	_bstr_t bstTargetWndClass(bsTargetWndClass);
	const DWORD dwTargetFullNameSize = _MAX_PATH;
	DWORD   dwRemote = 0;					// remote thread ID
	HANDLE   hRemote  = 0;					// remote thread handle
	FARPROC pLoadLibrary  = NULL;			// pointer to LoadLibrary function
	LPVOID   pRemotePlugin = NULL;			// remote plugin filename buffer
 
	LPCTSTR szFullTarget = bstTargetPath; // full name of target application
	LPCTSTR szTarget = _tcsrchr(szFullTarget, _T('\\'));
	if (0 < szTarget)
		szTarget++;
	else
		szTarget = szFullTarget;
	
	LPCTSTR szFullPluginName = bstPluginPath; // plugin module name
	LPCTSTR szTargetWndClass = bstTargetWndClass;

	HANDLE hProcess = GetProcessHandle(szTarget);
	if (0 == hProcess)
	{
		// Target application is not running. Thus, it has to be started
		GetWindowsDirectory((LPSTR)szFullTarget, sizeof(szFullTarget));

		STARTUPINFO infoTargetInit;			// process startup structure
		PROCESS_INFORMATION infoTarget;		// process information structure
		memset(&infoTargetInit, 0, sizeof(infoTargetInit));
		infoTargetInit.cb = sizeof(infoTargetInit);
		infoTargetInit.dwFlags = STARTF_USESHOWWINDOW;
		infoTargetInit.wShowWindow = SW_SHOWNORMAL;

		// Create target process
		CreateProcess(szFullTarget,						// application name
						   NULL,						// command line
						   NULL,						// process security
						   NULL,						// thread security
						   FALSE,						// inherit handles
						   CREATE_DEFAULT_ERROR_MODE,	// creation flags
						   NULL,						// environment
						   NULL,						// directory
						   &infoTargetInit,				// startup structure
						   &infoTarget);				// information structure

		hProcess = infoTarget.hProcess;
	}

	if (FAILED(CoInitialize(NULL)))
		return E_FAIL;

	IWndFinderPtr spWndFinder(__uuidof(WndFinder));
	if (NULL == spWndFinder)
		return E_FAIL;

	// Wait for main window of target application
	LONG lWnd = spWndFinder->GetWindow(_bstr_t(szTargetWndClass));
	if (0 >= lWnd)
		return E_FAIL;
	
	// Target application is running
	DWORD dwPluginNameSize  = (DWORD)_tcslen(szFullPluginName)+1;
	if (0 != hProcess)
		// Allocate buffer in target process address space
		pRemotePlugin = VirtualAllocEx(hProcess, NULL, dwPluginNameSize, MEM_COMMIT, PAGE_READWRITE);

	BOOL br = FALSE;
	if (NULL != pRemotePlugin)
		// Copy plugin library filename into remote buffer
		br = WriteProcessMemory(hProcess, pRemotePlugin, szFullPluginName, dwPluginNameSize, NULL);

	if (br)
	{
		// Get address of LoadLibrary function
		HMODULE hModule = GetModuleHandle(g_szKernel);
		if (0 != hModule)
			pLoadLibrary = GetProcAddress(hModule, g_szLoadLibrary);
	}

	if (NULL != pLoadLibrary)
		// Create remote thread to call LoadLibrary
		hRemote = CreateRemoteThread(hProcess,								// process
									  NULL,									// security
									  0,									// stack size
									  (LPTHREAD_START_ROUTINE)pLoadLibrary,	// function
									  pRemotePlugin,						// parameter
									  0,									// creation flags
									  NULL);								// thread ID
	
	if (0 != hRemote)
	{
		// Wait for remote thread to finish
		WaitForSingleObject(hRemote, INFINITE);
		GetExitCodeThread(hRemote, &dwRemote);
		CloseHandle(hRemote);
	}

	hr = (0 != dwRemote) ? /*Success!!*/S_OK : /*Failure??*/E_FAIL;

	if (0 != hProcess)
	{
		// Free resources
		VirtualFreeEx(hProcess, pRemotePlugin, 0, MEM_RELEASE);
		CloseHandle(hProcess);
	}

	return hr;
}
