window.onload = function() {
    var myShakeEvent = new Shake({
        threshold: 1
    });

    myShakeEvent.start();

    window.addEventListener('shake', shakeEventDidOccur, false);

    function shakeEventDidOccur () {
		var ShowCount = 1;
		var i;
		var str="";
		var titlestr="";
		var sImg = new Array();
		var sWord = new Array();
		sImg[0]="static/images/pic1.jpg";
		sImg[1]="static/images/pic2.jpg";



		sWord[0]="我想给你念句诗";
		sWord[1]="你最特别";



		function mixArray(source){
			var goal=[];
			for(var i=0;i<source.length;i++){
				var pos=Math.floor(Math.random()*(source.length-i));
				goal[i]=source[pos];
				source[pos]=source[source.length-1-i];
			}
			return goal;
		}

		var Ro = new Array();
		for (var x=0;x<sImg.length ;x++ ){
			Ro[x]=x;}
		Ro=mixArray(Ro);
		for (var j=0;j<ShowCount ; j++){
			str += "<img src=\"" + sImg[Ro[j]] + "\"height=\"100%\" width=\"100%\" />";
		    titlestr +="教师节，想和你说的——"+sWord[Ro[j]];
		}

		document.getElementById("main").innerHTML=str;
		document.title=titlestr;
	}
};