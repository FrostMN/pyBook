function cardView() {
    var con = document.getElementById('container');
    var type = con.childNodes;
    type[1].id = 'cards';
}

function listView() {
    var con = document.getElementById('container');
    var type = con.childNodes;
    type[1].id = 'lines';
}

function iconView() {
    var con = document.getElementById('container');
    var type = con.childNodes;
    type[1].id = 'icons';
}


function editBook(obj) {
    var editID = 'edit' + obj;
    var modal = document.getElementById(editID);
    modal.style.display = "block";
}

function lendBook(obj) {
    var lendID = 'lend' + obj;
    var modal = document.getElementById(lendID);
    modal.style.display = "block";
}

function hideBook(obj) {
    var hideID = 'hide' + obj;
    var modal = document.getElementById(hideID);
    modal.style.display = "block";
}

function closeModal(obj) {
    var closeID = obj;
    var modal = document.getElementById(closeID);
    document.getElementById("container").style.removeProperty("height");
    document.getElementById("container").style.removeProperty("overflow");
    modal.style.display = "none";
}