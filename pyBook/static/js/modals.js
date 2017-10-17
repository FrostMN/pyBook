

function editModal(title, fname, lname, isbn_10, isbn_13, book_img, synopsis, sort, stars, book_id) {

    if( sort === "None") {
        sort = stripLeadingArticle(title);
    }

    var escaped_title = escapeQuotes(title);
    var escaped_synopsis = escapeQuotes(synopsis);

    var star_select = document.createElement("select");
    star_select.setAttribute("name", "stars");
    star_select.setAttribute("id", "edit-form-select");
    star_select.setAttribute("form", "edit-form" + isbn_10);

    var unrated = document.createElement("option");
    unrated.setAttribute("value", "0");
    unrated.innerHTML = "unrated";

    var half_star = document.createElement("option");
    half_star.setAttribute("value", "0.5");
    half_star.innerHTML = "0.5";

    var one_star = document.createElement("option");
    one_star.setAttribute("value", "1.0");
    one_star.innerHTML = "1.0";

    var one_half_star = document.createElement("option");
    one_half_star.setAttribute("value", "1.5");
    one_half_star.innerHTML = "1.5";

    var two_star = document.createElement("option");
    two_star.setAttribute("value", "2.0");
    two_star.innerHTML = "2.0";

    var two_half_star = document.createElement("option");
    two_half_star.setAttribute("value", "2.5");
    two_half_star.innerHTML = "2.5";

    var three_star = document.createElement("option");
    three_star.setAttribute("value", "3.0");
    three_star.innerHTML = "3.0";

    var three_half_star = document.createElement("option");
    three_half_star.setAttribute("value", "3.5");
    three_half_star.innerHTML = "3.5";

    var four_star = document.createElement("option");
    four_star.setAttribute("value", "4.0");
    four_star.innerHTML = "4.0";

    var four_half_star = document.createElement("option");
    four_half_star.setAttribute("value", "4.5");
    four_half_star.innerHTML = "4.5";

    var five_star = document.createElement("option");
    five_star.setAttribute("value", "5.0");
    five_star.innerHTML = "5.0";

    star_select.appendChild(unrated);
    star_select.appendChild(half_star);
    star_select.appendChild(one_star);
    star_select.appendChild(one_half_star);
    star_select.appendChild(two_star);
    star_select.appendChild(two_half_star);
    star_select.appendChild(three_star);
    star_select.appendChild(three_half_star);
    star_select.appendChild(four_star);
    star_select.appendChild(four_half_star);
    star_select.appendChild(five_star);

    var modal = document.createElement("div");
    modal.setAttribute("id", "edit" + isbn_10);
    modal.setAttribute("class", "modal");

    var edit_modal = document.createElement("div");
    edit_modal.setAttribute("class", "edit-modal");

    var edit_thumb = document.createElement("div");
    edit_thumb.setAttribute("class", "edit-thumb");

    var edit_cover = document.createElement("img");
    edit_cover.setAttribute("class", "edit-cover");
    edit_cover.setAttribute("src", book_img);

    var edit_modal_text = document.createElement("div");
    edit_modal_text.setAttribute("class", "edit-modal-text");

    // create cancel link
    var cancel_modal = document.createElement("a");
    cancel_modal.setAttribute("class", "cancel-modal");
    cancel_modal.setAttribute("onclick", "closeModal('edit" + isbn_10 + "')");
    cancel_modal.setAttribute("href", "javascript:void(0);");

    // create cancel icon
    var cancel_icon = document.createElement("i");
    cancel_icon.setAttribute("class", "fa fa-times");
    cancel_icon.setAttribute("aria-hidden", "true");



    // create edit form
    var edit_form = document.createElement("form");
    edit_form.setAttribute("id", "edit-form" + isbn_10 );
    edit_form.setAttribute("action", "/edit");
    edit_form.setAttribute("method", "post");

    // create book_id hidden input
    var book_id_input = document.createElement("input");
    book_id_input.setAttribute("type", "hidden");
    book_id_input.setAttribute("name", "book_id");
    book_id_input.setAttribute("value", book_id);

    // create title label
    var title_label = document.createElement("label");
    title_label.setAttribute("for", "title");
    title_label.innerHTML = "Title: ";

    // create title text box
    var title_text_box = document.createElement("input");
    title_text_box.setAttribute("type", "text");
    title_text_box.setAttribute("name", "title");
    title_text_box.setAttribute("placeholder", "Title");
    title_text_box.setAttribute("value", title);
    //title_text_box.innerHTML = "Title: ";

    // create sort label
    var sort_label = document.createElement("label");
    sort_label.setAttribute("for", "title");
    sort_label.innerHTML = "Sort: ";

    // create sort text box
    var sort_text_box = document.createElement("input");
    sort_text_box.setAttribute("type", "text");
    sort_text_box.setAttribute("name", "sort");
    sort_text_box.setAttribute("placeholder", "Sort by");
    sort_text_box.setAttribute("value", sort);

    // create author label
    var author_label = document.createElement("label");
    author_label.setAttribute("for", "author_fname");
    author_label.innerHTML = "Author: ";

    // create author first name text box
    var fname_text_box = document.createElement("input");
    fname_text_box.setAttribute("type", "text");
    fname_text_box.setAttribute("name", "author_fname");
    fname_text_box.setAttribute("placeholder", "First");
    fname_text_box.setAttribute("value", fname);
    //fname_text_box.innerHTML = "Title: ";

    // create last name text box
    var lname_text_box = document.createElement("input");
    lname_text_box.setAttribute("type", "text");
    lname_text_box.setAttribute("name", "author_lname");
    lname_text_box.setAttribute("placeholder", "Last");
    lname_text_box.setAttribute("value", lname);
    //lname_text_box.innerHTML = "Title: ";

    // create isbn_10 label
    var isbn_10_label = document.createElement("label");
    isbn_10_label.setAttribute("for", "isbn_10");
    isbn_10_label.innerHTML = "ISBN 10: ";

    // create isbn_10 text box
    var isbn_10_text_box = document.createElement("input");
    isbn_10_text_box.setAttribute("type", "text");
    isbn_10_text_box.setAttribute("name", "isbn_10");
    isbn_10_text_box.setAttribute("placeholder", "ISBN 10");
    isbn_10_text_box.setAttribute("value", isbn_10);

    // create isbn_13 label
    var isbn_13_label = document.createElement("label");
    isbn_13_label.setAttribute("for", "isbn_13");
    isbn_13_label.innerHTML = "ISBN 10: ";

    // create isbn_13 text box
    var isbn_13_text_box = document.createElement("input");
    isbn_13_text_box.setAttribute("type", "text");
    isbn_13_text_box.setAttribute("name", "isbn_13");
    isbn_13_text_box.setAttribute("placeholder", "ISBN 13");
    isbn_13_text_box.setAttribute("value", isbn_13);

    // create submit button
    var edit_button = document.createElement("button");
    edit_button.setAttribute("type", "submit");
    edit_button.innerHTML = "Save";

    // create delete button
    var delete_button = document.createElement("button");
    delete_button.setAttribute("onclick", "deleteModal('" + isbn_10 + "', '" + book_id + "', '" + escaped_title +"')");
    delete_button.setAttribute("type", "button");
    delete_button.innerHTML = "Delete";

    // create isbn_13 label
    var synopsis_label = document.createElement("label");
    synopsis_label.setAttribute("for", "synopsis");
    synopsis_label.innerHTML = "Synopsis: ";


    var text_area = document.createElement("textarea");
    text_area.setAttribute("class", "edit-textarea");
    text_area.setAttribute("name", "synopsis");
    text_area.innerHTML = escaped_synopsis;


    // build edit-form from components
    edit_form.appendChild(book_id_input);

    edit_form.appendChild(title_label);
    edit_form.appendChild(title_text_box);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(sort_label);
    edit_form.appendChild(sort_text_box);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(author_label);
    edit_form.appendChild(fname_text_box);
    edit_form.appendChild(lname_text_box);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(isbn_10_label);
    edit_form.appendChild(isbn_10_text_box);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(isbn_13_label);
    edit_form.appendChild(isbn_13_text_box);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(synopsis_label);
    edit_form.appendChild(document.createElement('br'));
    edit_form.appendChild(text_area);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(star_select);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(delete_button);
    edit_form.appendChild(edit_button);


    // add <i> tag into <a>
    cancel_modal.appendChild(cancel_icon);


    // building <div class="edit-thumb">
    // add <img> to <div class="edit-thumb"...
    edit_thumb.appendChild(edit_cover);

    // building <div class="edit-modal-text">
    // add <a> tag into <div calss="edit-modal-text"... //
    edit_modal_text.appendChild(cancel_modal);

    // add <form> tag into <div calss="edit-modal-text"... //
    edit_modal_text.appendChild(edit_form);



    // building <div class="edit-modal">
    // add <div class="edit-thumb"> to <div class="edit-modal">
    edit_modal.appendChild(edit_thumb);
    // add <div class="edit-modal-text"> to <div class="edit-modal">
    edit_modal.appendChild(edit_modal_text);

    // building <div class="modal">
    // add <div class="edit-modal"> to <div class="modal">
    modal.appendChild(edit_modal);

    //alert("after appends");
    //alert(modal.textContent);

    document.getElementById("container").appendChild(modal);

    var editID = 'edit' + isbn_10;

    star_select.selectedIndex = getStarIndex(stars);


    //alert("editID: " + editID);
    document.getElementById(editID).style.display = "block";
    document.getElementById("container").style.height = "calc(100vh - 7em)";
    document.getElementById("container").style.overflow = "hidden";
}

function logInModal() {

    var modal = document.createElement("div");
    modal.setAttribute("id", "login");
    modal.setAttribute("class", "modal");
    modal.setAttribute("onclick", "closeModal('login')");


    var login_modal = document.createElement("div");
    login_modal.setAttribute("class", "login-modal");


    var login_form = document.createElement("form");
    login_form.setAttribute("action", "/log_in");
    login_form.setAttribute("method", "POST");



    var uname_label = document.createElement("label");
    uname_label.setAttribute("for", "uname");
    uname_label.innerHTML = "User Name: ";

    var uname_input = document.createElement("input");
    uname_input.setAttribute("name", "uname");
    uname_input.setAttribute("type", "text");

    var pword_label = document.createElement("label");
    pword_label.setAttribute("for", "pword");
    pword_label.innerHTML = " Password: ";

    var pword_input = document.createElement("input");
    pword_input.setAttribute("name", "pword");
    pword_input.setAttribute("type", "password");

    var login_submit = document.createElement("button");
    login_submit.setAttribute("type", "submit");
    login_submit.innerHTML = "login";

    login_form.appendChild(uname_label);
    login_form.appendChild(uname_input);
    login_form.appendChild(document.createElement('br'));
    login_form.appendChild(pword_label);
    login_form.appendChild(pword_input);
    login_form.appendChild(document.createElement('br'));
    login_form.appendChild(login_submit);

    login_modal.appendChild(login_form);

    modal.appendChild(login_modal);



    document.getElementById("container").appendChild(modal);

    document.getElementById("login").style.display = "block";
    document.getElementById("container").style.height = "calc(100vh - 7em)";
    document.getElementById("container").style.overflow = "hidden";
    uname_input.focus();

}

function lendBook(book_id, api_key, users_json) {
    var users = JSON.parse(users_json);

    var modal = document.createElement("div");
    modal.setAttribute("id", "lend-book-" + book_id);
    modal.setAttribute("class", "modal");
    modal.setAttribute("onclick", "clodeModal(lend-book-" + book_id);


    var lend_modal = document.createElement("div");
    lend_modal.setAttribute("class", "lend-modal");

    var lend_form = document.createElement("form");
    lend_form.setAttribute("action", "/api/v1/" + api_key + "/books/" + book_id);
    lend_form.setAttribute("method", "POST");

    var put_input = document.createElement("input");
    put_input.setAttribute("type", "hidden");
    put_input.setAttribute("name", "_method");
    put_input.setAttribute("value", "PUT");


    var select_user = document.createElement("select");
    select_user.setAttribute("name", "user");

    for (var i = 1; i < users.length; i++) {
        var user = document.createElement("option");
        var value = users[i].id + ";" + users[i].fname + ";" + users[i].lname;
        user.setAttribute("value", value);
        user.innerHTML = users[i].fname + " " + users[i].lname;
        select_user.appendChild(user);
    }

    var submit_button = document.createElement("button");
    submit_button.innerHTML = "lend";

    modal.appendChild(lend_modal);
    lend_modal.appendChild(lend_form);
    lend_form.appendChild(put_input);
    lend_form.appendChild(select_user);
    lend_form.appendChild(submit_button);

    document.getElementById("container").appendChild(modal);

    document.getElementById("lend-book-" + book_id).style.display = "block";
    document.getElementById("container").style.height = "calc(100vh - 7em)";
    document.getElementById("container").style.overflow = "hidden";
}

function returnBook(book_id, api_key, lendee) {
    alert("book_id: " + book_id + " api_key: " + api_key + " lendee: " + lendee);




}

function addBookModal(api_key) {

    // alert(api_key);

    var modal = document.createElement("div");
    modal.setAttribute("id", "add-book");
    modal.setAttribute("class", "modal");
    modal.setAttribute("onclick", "closeModal(add-book)");



    var add_book_modal = document.createElement("div");
    add_book_modal.setAttribute("class", "add-book-modal");

    var isbn_label = document.createElement("label");
    isbn_label.setAttribute("for", "isbn");
    isbn_label.innerHTML = "ISBN: ";

    var isbn_box = document.createElement("input");
    isbn_box.setAttribute("name", "isbn");
    isbn_box.setAttribute("type", "text");
    isbn_box.setAttribute("onkeydown", "addBook('" + api_key + "', document.getElementById('add-by-isbn').value, event)");
    isbn_box.setAttribute("id", "add-by-isbn");

    var isbn_button = document.createElement("button");
    isbn_button.setAttribute("onclick", "addBook('" + api_key + "', document.getElementById('add-by-isbn').value, event)");
    isbn_button.innerHTML = "Search";

    add_book_modal.appendChild(isbn_label);
    add_book_modal.appendChild(isbn_box);
    add_book_modal.appendChild(isbn_button);

    modal.appendChild(add_book_modal);
    document.getElementById("container").appendChild(modal);

    document.getElementById("add-book").style.display = "block";
    document.getElementById("container").style.height = "calc(100vh - 7em)";
    document.getElementById("container").style.overflow = "hidden";

    isbn_box.focus();
}

// I found the getJSON and parts of the addBook function from stack overflow           //
// https://stackoverflow.com/questions/12460378/how-to-get-json-from-url-in-javascript //

function addBook(api_key, isbn) {
    if ((event.keyCode === 13) || (event.type === "click")) {
        if (isbn !== "") {    // TODO add an isbn validation method somewhere
            getJSON("/api/add/" + api_key + "/" + isbn, function (err, book) {
                //alert("http://127.0.0.1:5000/api/" + isbn);
                if (err !== null) {
                    alert('Something went wrong: ' + err);
                } else {
                    // parse json response from api to propagate forms
                    var auth_fname = book.author.split(" ")[0];
                    var auth_lname = book.author.split(" ")[1];

                    closeModal('add-book');
                    var mod = document.getElementById('add-book');
                    mod.outerHTML = "";
                    delete mod;
                    newBookModal(book.title, auth_fname, auth_lname, book.isbn_10, book.isbn_13, book.image, book.synopsis, "None");
                }
            });
        }
    }
}

var getJSON = function(url, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', url, true);
    xhr.responseType = 'json';
    xhr.onload = function() {
      var status = xhr.status;
      if (status === 200) {
          // for (var name in xhr.response) {
          // }
        callback(null, xhr.response);
      } else {
        callback(status, xhr.response);
      }
    };
    xhr.send();
};



function newBookModal(title, fname, lname, isbn_10, isbn_13, book_img, synopsis, sort, book_id) {

    if( sort === "None") {
        sort = stripLeadingArticle(title);
    }

    var api_img_url = 'http://covers.openlibrary.org/b/isbn/' + isbn_10 + '-L.jpg';
    var file_name = sort.substring(0,5) + isbn_10;

    book_img = api_img_url;

    if (title === 'not found') {
        book_img = '/static/img/covers/default.jpg';
        file_name = "default.jpg";
    }


    var newBookID = 'new' + isbn_10;

    var star_select = document.createElement("select");
    star_select.setAttribute("name", "stars");
    star_select.setAttribute("id", "edit-form-select");
    star_select.setAttribute("form", "new-book-form" + isbn_10);

    var unrated = document.createElement("option");
    unrated.setAttribute("value", "0");
    unrated.innerHTML = "unrated";

    var half_star = document.createElement("option");
    half_star.setAttribute("value", "0.5");
    half_star.innerHTML = "0.5";

    var one_star = document.createElement("option");
    one_star.setAttribute("value", "1.0");
    one_star.innerHTML = "1.0";

    var one_half_star = document.createElement("option");
    one_half_star.setAttribute("value", "1.5");
    one_half_star.innerHTML = "1.5";

    var two_star = document.createElement("option");
    two_star.setAttribute("value", "2.0");
    two_star.innerHTML = "2.0";

    var two_half_star = document.createElement("option");
    two_half_star.setAttribute("value", "2.5");
    two_half_star.innerHTML = "2.5";

    var three_star = document.createElement("option");
    three_star.setAttribute("value", "3.0");
    three_star.innerHTML = "3.0";

    var three_half_star = document.createElement("option");
    three_half_star.setAttribute("value", "3.5");
    three_half_star.innerHTML = "3.5";

    var four_star = document.createElement("option");
    four_star.setAttribute("value", "4.0");
    four_star.innerHTML = "4.0";

    var four_half_star = document.createElement("option");
    four_half_star.setAttribute("value", "4.5");
    four_half_star.innerHTML = "4.5";

    var five_star = document.createElement("option");
    five_star.setAttribute("value", "5.0");
    five_star.innerHTML = "5.0";

    star_select.appendChild(unrated);
    star_select.appendChild(half_star);
    star_select.appendChild(one_star);
    star_select.appendChild(one_half_star);
    star_select.appendChild(two_star);
    star_select.appendChild(two_half_star);
    star_select.appendChild(three_star);
    star_select.appendChild(three_half_star);
    star_select.appendChild(four_star);
    star_select.appendChild(four_half_star);
    star_select.appendChild(five_star);

    var modal = document.createElement("div");
    modal.setAttribute("id", newBookID);
    modal.setAttribute("class", "modal");

    var edit_modal = document.createElement("div");
    edit_modal.setAttribute("class", "new-book-modal");

    var edit_thumb = document.createElement("div");
    edit_thumb.setAttribute("class", "new-book-thumb");

    var edit_cover = document.createElement("img");
    edit_cover.setAttribute("class", "edit-cover");
    edit_cover.setAttribute("src", book_img);

    var edit_modal_text = document.createElement("div");
    edit_modal_text.setAttribute("class", "new-book-modal-text");

    // create cancel link
    var cancel_modal = document.createElement("a");
    cancel_modal.setAttribute("class", "cancel-modal");
    cancel_modal.setAttribute("onclick", "closeModal('" + newBookID + "')");
    cancel_modal.setAttribute("href", "javascript:void(0);");

    // create cancel icon
    var cancel_icon = document.createElement("i");
    cancel_icon.setAttribute("class", "fa fa-times");
    cancel_icon.setAttribute("aria-hidden", "true");


    // create edit form
    var edit_form = document.createElement("form");
    edit_form.setAttribute("id", "new-book-form" + isbn_10 );
    edit_form.setAttribute("action", "/add");
    edit_form.setAttribute("method", "post");

    // create book_id hidden input
    var book_id_input = document.createElement("input");
    book_id_input.setAttribute("type", "hidden");
    book_id_input.setAttribute("name", "book_id");
    book_id_input.setAttribute("value", book_id);

    // create image_url hidden input
    var image_url_input = document.createElement("input");
    image_url_input.setAttribute("type", "hidden");
    image_url_input.setAttribute("name", "image_url");
    image_url_input.setAttribute("value", book_img);

    // create image_name hidden input
    var image_name = document.createElement("input");
    image_name.setAttribute("type", "hidden");
    image_name.setAttribute("name", "image_name");
    image_name.setAttribute("value", file_name);

    // create title label
    var title_label = document.createElement("label");
    title_label.setAttribute("for", "title");
    title_label.innerHTML = "Title: ";

    // create title text box
    var title_text_box = document.createElement("input");
    title_text_box.setAttribute("type", "text");
    title_text_box.setAttribute("name", "title");
    title_text_box.setAttribute("placeholder", "Title");
    title_text_box.setAttribute("value", title);

    // create sort label
    var sort_label = document.createElement("label");
    sort_label.setAttribute("for", "title");
    sort_label.innerHTML = "Sort: ";

    // create sort text box
    var sort_text_box = document.createElement("input");
    sort_text_box.setAttribute("type", "text");
    sort_text_box.setAttribute("name", "sort");
    sort_text_box.setAttribute("placeholder", "Sort by");
    sort_text_box.setAttribute("value", sort);

    // create author label
    var author_label = document.createElement("label");
    author_label.setAttribute("for", "author_fname");
    author_label.innerHTML = "Author:  ";

    // create author first name text box
    var fname_text_box = document.createElement("input");
    fname_text_box.setAttribute("type", "text");
    fname_text_box.setAttribute("name", "author_fname");
    fname_text_box.setAttribute("placeholder", "First");
    fname_text_box.setAttribute("value", fname);
    //fname_text_box.innerHTML = "Title: ";

    // create last name text box
    var lname_text_box = document.createElement("input");
    lname_text_box.setAttribute("type", "text");
    lname_text_box.setAttribute("name", "author_lname");
    lname_text_box.setAttribute("placeholder", "Last");
    lname_text_box.setAttribute("value", lname);
    //lname_text_box.innerHTML = "Title: ";

    // create isbn_10 label
    var isbn_10_label = document.createElement("label");
    isbn_10_label.setAttribute("for", "isbn_10");
    isbn_10_label.innerHTML = "ISBN 10: ";

    // create isbn_10 text box
    var isbn_10_text_box = document.createElement("input");
    isbn_10_text_box.setAttribute("type", "text");
    isbn_10_text_box.setAttribute("name", "isbn_10");
    isbn_10_text_box.setAttribute("placeholder", "ISBN 10");
    isbn_10_text_box.setAttribute("value", isbn_10);

    // create isbn_13 label
    var isbn_13_label = document.createElement("label");
    isbn_13_label.setAttribute("for", "isbn_13");
    isbn_13_label.innerHTML = "ISBN 10: ";

    // create isbn_13 text box
    var isbn_13_text_box = document.createElement("input");
    isbn_13_text_box.setAttribute("type", "text");
    isbn_13_text_box.setAttribute("name", "isbn_13");
    isbn_13_text_box.setAttribute("placeholder", "ISBN 13");
    isbn_13_text_box.setAttribute("value", isbn_13);

    // create submit button
    var edit_button = document.createElement("button");
    edit_button.setAttribute("type", "submit");
    edit_button.innerHTML = "Save";

    // create isbn_13 label
    var synopsis_label = document.createElement("label");
    synopsis_label.setAttribute("for", "synopsis");
    synopsis_label.innerHTML = "Synopsis: ";


    var text_area = document.createElement("textarea");
    text_area.setAttribute("class", "new-book-textarea");
    text_area.setAttribute("name", "synopsis");
    text_area.innerHTML = synopsis;


    // build edit-form from components
    edit_form.appendChild(book_id_input);
    edit_form.appendChild(image_url_input);
    edit_form.appendChild(image_name);

    edit_form.appendChild(title_label);
    edit_form.appendChild(title_text_box);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(sort_label);
    edit_form.appendChild(sort_text_box);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(author_label);
    edit_form.appendChild(fname_text_box);
    edit_form.appendChild(lname_text_box);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(isbn_10_label);
    edit_form.appendChild(isbn_10_text_box);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(isbn_13_label);
    edit_form.appendChild(isbn_13_text_box);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(synopsis_label);
    edit_form.appendChild(document.createElement('br'));
    edit_form.appendChild(text_area);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(star_select);

    edit_form.appendChild(document.createElement('br'));


    edit_form.appendChild(edit_button);


    // add <i> tag into <a>
    cancel_modal.appendChild(cancel_icon);


    // building <div class="edit-thumb">
    // add <img> to <div class="edit-thumb"...
    edit_thumb.appendChild(edit_cover);

    // building <div class="edit-modal-text">
    // add <a> tag into <div calss="edit-modal-text"... //
    edit_modal_text.appendChild(cancel_modal);

    // add <form> tag into <div calss="edit-modal-text"... //
    edit_modal_text.appendChild(edit_form);

    // building <div class="edit-modal">
    // add <div class="edit-thumb"> to <div class="edit-modal">
    edit_modal.appendChild(edit_thumb);
    // add <div class="edit-modal-text"> to <div class="edit-modal">
    edit_modal.appendChild(edit_modal_text);

    // building <div class="modal">
    // add <div class="edit-modal"> to <div class="modal">
    modal.appendChild(edit_modal);

    //alert("after appends");
    //alert(modal.textContent);

    document.getElementById("container").appendChild(modal);


    //alert("newBookID: " + newBookID);
    document.getElementById(newBookID).style.display = "block";
    document.getElementById("container").style.height = "calc(100vh - 7em)";
    document.getElementById("container").style.overflow = "hidden";
}

// converts star number in book object to html select index
function getStarIndex(stars) {
    if (stars === "0.0") {
        return 0;
    }
    if (stars === "0.5") {
        return 1;
    }
    if (stars === "1.0") {
        return 2;
    }
    if (stars === "1.5") {
        return 3;
    }
    if (stars === "2.0") {
        return 4;
    }
    if (stars === "2.5") {
        return 5;
    }
    if (stars === "3.0") {
        return 6;
    }
    if (stars === "3.5") {
        return 7;
    }
    if (stars === "4.0") {
        return 8;
    }
    if (stars === "4.5") {
        return 9;
    }
    if (stars === "5.0") {
        return 10;
    }
}

function deleteModal(isbn_10, book_id, title) {
    // create book_id hidden input
    var book_id_input = document.createElement("input");
    book_id_input.setAttribute("type", "hidden");
    book_id_input.setAttribute("name", "book_id");
    book_id_input.setAttribute("value", book_id);

    var delete_modal = document.createElement('div');
    delete_modal.setAttribute("id", "delete" + isbn_10 );
    delete_modal.setAttribute("class", "delete-modal");

    var delete_form = document.createElement('form');
    delete_form.setAttribute("action", "/delete");
    delete_form.setAttribute("method", "post");

    var delete_button = document.createElement("button");
    delete_button.setAttribute("type", "submit");
    delete_button.innerHTML = "Delete";

    var cancel_button = document.createElement("button");
    cancel_button.setAttribute("type", "button");
    cancel_button.setAttribute("onclick", "closeModal('delete" + isbn_10 + "')");
    cancel_button.innerHTML = "Cancel";

    var delete_warning = document.createElement('h2');
    delete_warning.innerHTML = "Are you sure you want to delete:?";

    var title_header = document.createElement('h3');
    title_header.innerHTML = title;

    delete_form.appendChild(book_id_input);
    delete_form.appendChild(cancel_button);
    delete_form.appendChild(delete_button);

    delete_modal.appendChild(delete_warning);
    delete_modal.appendChild(title_header);
    delete_modal.appendChild(delete_form);

    var outer_modal = document.getElementById('edit' + isbn_10);
    outer_modal.appendChild(delete_modal);
}

function stripLeadingArticle(title) {
    var stripped = "";
    if (title.substring(0, 4) === "The ") {
        //alert(title.substring(0, 3));
        stripped = title.substring(4);
    } else if (title.substring(0, 2) === "A ") {
        stripped = title.substring(2);
    } else if (title.substring(0, 4) === "the ") {
        stripped = title.substring(4);
    } else if (title.substring(0, 2) === "a ") {
        stripped = title.substring(2);
    } else {
        stripped = title;
    }
    return stripped;
}

function escapeQuotes(string) {
    var escaped_string = string.replace("'", "&rsquo;");
    escaped_string = escaped_string.replace('"', "&quot;");
    return escaped_string;
}
//
// function closeModal() {
//
// }


function closeModal(obj) {
    var closeID = obj;
    var modal = document.getElementById(closeID);
    document.getElementById("container").style.removeProperty("height");
    document.getElementById("container").style.removeProperty("overflow");
    modal.style.display = "none";
}

