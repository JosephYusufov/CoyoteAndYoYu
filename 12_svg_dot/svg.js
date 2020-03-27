var pic = document.getElementById("vimage");
var c = document.createElementNS("http://www.w3.org/2000/svg", "circle");
c.setAttribute("cx", 400);
c.setAttribute("cy", 100);
c.setAttribute("r", 100);
c.setAttribute("fill", "red");
c.setAttribute("stroke", "black");
pic.appendChild(c);
