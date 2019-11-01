$(function(){
	var subPage = new Array;
	subPage[0] = "account";
	subPage[1] = "bgm";
	subPage[2] = "photo";
	subPage[3] = "community";
	subPage[4] = "upload";
	subPage[5] = "customer";
    subPage[6] = "team";

	var url = location.href;
	var getAr0 = url.indexOf(subPage[0]);
	var getAr1 = url.indexOf(subPage[1]);
	var getAr2 = url.indexOf(subPage[2]);
	var getAr3 = url.indexOf(subPage[3]);
	var getAr4 = url.indexOf(subPage[4]);
	var getAr5 = url.indexOf(subPage[5]);
	var getAr6 = url.indexOf(subPage[6]);

	if(getAr0 != -1){
		$("li:eq(1) a").addClass("on")
	};
	if(getAr1 != -1){
		$("li:eq(2) a").addClass("on")
	};
	if(getAr2 != -1){
		$("li:eq(3) a").addClass("on")
	};
	if(getAr3 != -1){
		$("li:eq(4) a").addClass("on")
	};
	if(getAr4 != -1){
		$("li:eq(5) a").addClass("on")
	};
	if(getAr5 != -1){
		$("li:eq(6) a").addClass("on")
	};
	if(getAr6 != -1){
		$("li:eq(7) a").addClass("on")
	};
});