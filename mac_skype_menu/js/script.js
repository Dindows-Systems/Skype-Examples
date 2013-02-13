/*
* Author:      Marco Kuiper (http://www.marcofolio.net/)
*/
google.load("jquery", "1.3.1");
google.setOnLoadCallback(function()
{
	addSkypeDetails();
	
	// When a skype name is click, expand it
	$(".skypename").click(function () {
		expandSkype($(this));
	});
});

function expandSkype(parentElem) {
	addSkypeDetails();
	$(parentElem).children().remove();
	$(".expanded").removeClass("expanded");
	$(".expandeduser").removeClass("expandeduser");
	
	$(".skypeinfo").hide();
	$(parentElem).parent().addClass("expandeduser");
	$(parentElem)
		.addClass("expanded")
		.next().show();
}

function addSkypeDetails() {
	$(".extrainfo").remove();
	
	// Copy the "skypedetails" when not expanded
	$(".skypedetails").each(function() {
		var detailText = $(this).text();
		
		if(detailText.length > 40) {
			detailText = detailText.substring(0, 40) + "...";
		}
		
		$(this).parent().prev().append('<span class="extrainfo">'+ detailText +'</span>');	
	});
}