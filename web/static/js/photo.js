function doImgPop(img){
 img1= new Image();
 img1.src=(img);
 imgControll(img);
}

function imgControll(img){
 if((img1.width!=0)&&(img1.height!=0)){
    viewImage(img);
  }
  else{
     controller="imgControll('"+img+"')";
     intervalID=setTimeout(controller,20);
  }
}

function viewImage(img){
 W=img1.width;
 H=img1.height;
 LeftPosition=(screen.width-1000)/2;
 TopPosition=(screen.height-667)/2;

 O="width="+1000+",height="+667+",top="+TopPosition+",left="+LeftPosition+",scrollbars=yes";
 imgWin=window.open("","",O);
 imgWin.document.write("<html><head><title>:*:*:*: 이미지상세보기 :*:*:*:*:*:*:</title></head>");
 imgWin.document.write("<body topmargin=0 leftmargin=0>");
 imgWin.document.write("<img src="+img+" onclick='self.close()' style='cursor:pointer; width: 1000px; height: 667px;' title ='클릭하시면 창이 닫힙니다.'>");
 imgWin.document.close();
}