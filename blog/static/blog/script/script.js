function markAsSeen(user, recordId) {
    var xhttp = new XMLHttpRequest();
    url = "/user/" + user + "/record/" + recordId + "/"
    xhttp.open("GET", url, true);
    xhttp.send();
    var recordDiv = document.getElementById(recordId);
    var eyeDiv = recordDiv.firstElementChild.firstElementChild;
    var oldUrl = eyeDiv.src;
    var newUrl = eyeDiv.getAttribute('switch');
    eyeDiv.src = newUrl;
    eyeDiv.setAttribute('switch', oldUrl);
}