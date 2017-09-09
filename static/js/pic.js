window.onload = function() {
    var myShakeEvent = new Shake({
        threshold: 5
    });

    myShakeEvent.start();

    window.addEventListener('shake', shakeEventDidOccur, false);
    imgNum = 3;
    var sImg = new Array();
    var sImg1 = new Array();
    var sImg2 = new Array();
    var sImg3 = new Array();
    var sWord = new Array();
    var sWord1 = new Array();
    var sWord2 = new Array();
    var sWord3 = new Array();
    sImg1[0]="static/images/1_1.jpg";
    sImg1[1]="static/images/1_2.jpg";
    sImg1[2]="static/images/1_3.jpg";
    sImg1[3]="static/images/1_4.jpg";
    sImg1[4]="static/images/1_5.jpg";
    sImg1[5]="static/images/1_6.jpg";
    sImg2[0]="static/images/2_1.jpg";
    sImg2[1]="static/images/2_2.jpg";
    sImg2[2]="static/images/2_3.jpg";
    sImg2[3]="static/images/2_4.jpg";
    sImg2[4]="static/images/2_5.jpg";
    sImg2[5]="static/images/2_6.jpg";
    sImg2[6]="static/images/2_7.jpg";
    sImg2[7]="static/images/2_8.jpg";
    sImg2[8]="static/images/2_9.jpg";
    sImg2[9]="static/images/2_10.jpg";
    sImg2[10]="static/images/2_11.jpg";
    sImg2[11]="static/images/2_12.jpg";
    sImg2[12]="static/images/2_13.jpg";
    sImg2[13]="static/images/2_14.jpg";
    sImg2[14]="static/images/2_15.jpg";
    sImg3[0]="static/images/3_1.jpg";
    sImg3[1]="static/images/3_2.jpg";
    sImg3[2]="static/images/3_3.jpg";
    sImg3[3]="static/images/3_4.jpg";
    sImg3[4]="static/images/3_5.jpg";
    sImg3[5]="static/images/3_6.jpg";
    sImg3[6]="static/images/3_7.jpg";
    sImg3[7]="static/images/3_8.jpg";
    sImg3[8]="static/images/3_9.jpg";
    sImg3[9]="static/images/3_10.jpg";
    sImg3[10]="static/images/3_11.jpg";
    sImg3[11]="static/images/3_12.jpg";
    sImg3[12]="static/images/3_13.jpg";
    sImg3[13]="static/images/3_14.jpg";
    sImg3[14]="static/images/3_15.jpg";
    sImg3[15]="static/images/3_16.jpg";
    sImg3[16]="static/images/3_17.jpg";
    sImg3[17]="static/images/3_18.jpg";
    sImg3[18]="static/images/3_19.jpg";
    scan_page = "static/images/scan_page.jpg";

//
//    sImg2[0]="static/images/pic2.jpg";
//    sImg2[1]="static/images/pic2.jpg";
//    sImg3[0]="static/images/pic3.jpg";
//    sImg3[1]="static/images/pic3.jpg";

    sWord1[0]="我想给你念句诗";
    sWord1[1]="给你念句诗";
    sWord2[0]="你最特别";
    sWord2[1]="特别";
    sWord3[0]="谢谢你";
    sWord3[1]="你";
    title = '那些年老师说过的段子'

    function mixArray(source){
			var goal=[];
			for(var i=0;i<source.length;i++){
				var pos=Math.floor(Math.random()*(source.length-i));
				goal[i]=source[pos];
				source[pos]=source[source.length-1-i];
			}
			return goal;
	}
	Ro1 = new Array();
	Ro2 = new Array();
	Ro3 = new Array();
	maxImgSize = Math.max(sImg1.length,sImg2.length,sImg3.length);
    for (var x=0;x<sImg1.length ;x++ ){
        Ro1[x]=x;}
    for (var x=0;x<sImg2.length ;x++ ){
        Ro2[x]=x;}
    for (var x=0;x<sImg3.length ;x++ ){
        Ro3[x]=x;}
	Ro1=mixArray(Ro1);
	Ro2=mixArray(Ro2);
	Ro3=mixArray(Ro3);
	for (var i=0; i < maxImgSize; i++){
	    if(i<sImg1.length){
	        sImg[sImg.length] = sImg1[Ro1[i]];
	    }
	    if(i<sImg2.length){
	        sImg[sImg.length] = sImg2[Ro2[i]];
	    }
	    if(i<sImg3.length){
	        sImg[sImg.length] = sImg3[Ro3[i]];
	    }
//	    sImg[i*3] = sImg1[Ro[i]]
//	    sImg[i*3+1] = sImg2[Ro[i]]
//	    sImg[i*3+2] = sImg3[Ro[i]]
//	    sWord[i*3] = sWord1[Ro[i]]
//	    sWord[i*3+1] = sWord2[Ro[i]]
//	    sWord[i*3+2] = sWord3[Ro[i]]
	}
	sImg[sImg.length] = scan_page;
    j = 0;
    function shakeEventDidOccur () {
		var ShowCount = 1;
		var i;
		var str="";
		var titlestr="";

        str += "<img src=\"" + sImg[j] + "\"height=\"100%\" width=\"100%\" />";
//		titlestr +="教师节，想和你说的——"+sWord[j];
        titlestr = title;
		j=j+1;
		if(j >= sImg.length){
		    j=0;
		}

//		for (var j=0;j<ShowCount ; j++){
//			str += "<img src=\"" + sImg[Ro[j]] + "\"height=\"100%\" width=\"100%\" />";
//		    titlestr +="教师节，想和你说的——"+sWord[Ro[j]];
//		}

		document.getElementById("main").innerHTML=str;
		document.title=titlestr;
	}
};