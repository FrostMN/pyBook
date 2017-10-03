

function editModal(title, fname, lname, isbn_10, isbn_13, book_img, synopsis, book_id) {

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
    edit_form.setAttribute("action", "/save");
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

    // create isbn_13 label
    var synopsis_label = document.createElement("label");
    synopsis_label.setAttribute("for", "synopsis");
    synopsis_label.innerHTML = "Synopsis: ";


    var text_area = document.createElement("textarea");
    text_area.setAttribute("class", "edit-textarea");
    text_area.setAttribute("name", "synopsis");
    text_area.innerHTML = synopsis;


    // build edit-form from components
    edit_form.appendChild(book_id_input);

    edit_form.appendChild(title_label);
    edit_form.appendChild(title_text_box);

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

    //alert("editID: " + editID);
    document.getElementById(editID).style.display = "block";
    document.getElementById("container").style.height = "calc(100vh - 7em)";
    document.getElementById("container").style.overflow = "hidden";
}

function logInModal() {

    var modal = document.createElement("div");
    modal.setAttribute("id", "login");
    modal.setAttribute("class", "modal");


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

function lendModal(book) {
    console.log(book);
}

function addBook() {
    alert("in addBook()")
}
