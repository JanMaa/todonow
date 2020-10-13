function openNav() {
  if (screen.width <= 768) {
  	document.getElementById("mySidenav").style.width = "100%";
  }else{
  	document.getElementById("mySidenav").style.width = "300px";
  	document.getElementById("body_container").style.marginLeft = "300px";
    document.getElementById("inner").style.marginLeft = "300px";
  }
  document.getElementById("userBtn").style.visibility = "hidden";
}

function closeNav() {
	document.getElementById("mySidenav").style.width = "0";
  if (screen.width > 768) {
  	  document.getElementById("body_container").style.marginLeft= "0";
      document.getElementById("inner").style.marginLeft = "0";
  }
  document.getElementById("userBtn").style.visibility = "visible";
}