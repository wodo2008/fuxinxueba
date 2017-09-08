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
    sImg1[0]="static/images/pic1.jpg";
    sImg2[0]="static/images/pic2.jpg";
    sImg3[0]="static/images/pic3.jpg";

    sWord1[0]="我想给你念句诗";
    sWord2[0]="你最特别";
    sWord3[0]="谢谢你";

    function mixArray(source){
			var goal=[];
			for(var i=0;i<source.length;i++){
				var pos=Math.floor(Math.random()*(source.length-i));
				goal[i]=source[pos];
				source[pos]=source[source.length-1-i];
			}
			return goal;
	}
	Ro = new Array();
    for (var x=0;x<imgNum ;x++ ){
        Ro[x]=x;}
	Ro=mixArray(Ro);
	for (var i=0; i < Ro.length; i++){
	    sImg[i*3] = sImg1[Ro[i]]
	    sImg[i*3+1] = sImg2[Ro[i]]
	    sImg[i*3+2] = sImg3[Ro[i]]
	    sWord[i*3] = sWord1[Ro[i]]
	    sWord[i*3+1] = sWord2[Ro[i]]
	    sWord[i*3+2] = sWord3[Ro[i]]
	}
    j = 0;
    function shakeEventDidOccur () {
		var ShowCount = 1;
		var i;
		var str="";
		var titlestr="";

        str += "<img src=\"" + sImg[j] + "\"height=\"100%\" width=\"100%\" />";
		titlestr +="教师节，想和你说的——"+sWord[j];
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