function sideMenu() {
    var x = document.getElementById("menuLink");
    if (x.className === "menuButton") {
        x.className += " active";
    } else {
        x.className = "menuButton";
    }
    
    var x = document.getElementById("menu");
    if (x.className === "active") {
        x.className = "";
    } else {
        x.className = "active";
    }
    
    var x = document.getElementsByTagName('html')[0];
    if (x.className === "inactive") {
        x.className = "";
    } else {
        x.className = "inactive";
    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function UpdateTask(event) {
	let data = {TaskID: event.target.id, Value: event.target.checked};
	//console.log(data);
	fetch("/taskUpdate", {
		  method: "POST", 
		  body: JSON.stringify(data),
		  credentials: 'same-origin',
		  headers: {
		        "X-CSRFToken": getCookie("csrftoken"),
		        "Accept": "application/json",
		        "Content-Type": "application/json"
		    },
		}).then(res => {
		  //console.log("Request complete! response:", res);
		  location.reload(true);
		});
}

function overlay() {
	el = document.getElementById("overlay");
	el.className = (el.className == "hide") ? "show" : "hide";
	af = document.getElementsByName("taskName");
	if (el.className == "show") {af[0].focus()}
}





