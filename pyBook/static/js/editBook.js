

function editModal(title, fname, lname, isbn10, isbn13, book_img, synopsis) {
    alert("ineditmodal");

    //alert(book);


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
    cancel_modal.setAttribute("onclick", "closeModal('edit" + isbn10 + "')");
    cancel_modal.setAttribute("href", "javascript:void(0);");

    // create cancel icon
    var cancel_icon = document.createElement("i");
    cancel_icon.setAttribute("class", "fa fa-times");
    cancel_icon.setAttribute("aria-hidden", "true");



    // create edit form
    var edit_form = document.createElement("form");
    edit_form.setAttribute("id", "edit-form" + isbn10 );
    edit_form.setAttribute("action", "/save");
    edit_form.setAttribute("method", "post");

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

    // create isbn10 label
    var isbn10_label = document.createElement("label");
    isbn10_label.setAttribute("for", "isbn10");
    isbn10_label.innerHTML = "ISBN 10: ";

    // create isbn10 text box
    var isbn10_text_box = document.createElement("input");
    isbn10_text_box.setAttribute("type", "text");
    isbn10_text_box.setAttribute("name", "isbn10");
    isbn10_text_box.setAttribute("placeholder", "ISBN 10");
    isbn10_text_box.setAttribute("value", isbn10);

    // create isbn13 label
    var isbn13_label = document.createElement("label");
    isbn13_label.setAttribute("for", "isbn13");
    isbn13_label.innerHTML = "ISBN 10: ";

    // create isbn13 text box
    var isbn13_text_box = document.createElement("input");
    isbn13_text_box.setAttribute("type", "text");
    isbn13_text_box.setAttribute("name", "isbn13");
    isbn13_text_box.setAttribute("placeholder", "ISBN 13");
    isbn13_text_box.setAttribute("value", isbn13);

    // create submit button
    var edit_button = document.createElement("button");
    edit_button.setAttribute("type", "submit");
    edit_button.innerHTML = "Save";

    // create isbn13 label
    var synopsis_label = document.createElement("label");
    synopsis_label.setAttribute("for", "synopsis");
    synopsis_label.innerHTML = "Synopsis: ";


    var text_area = document.createElement("textarea");
    text_area.setAttribute("class", "edit-textarea");
    text_area.setAttribute("name", "synopsis");
    text_area.innerHTML = synopsis;


    // build edit-form from components
    edit_form.appendChild(title_label);
    edit_form.appendChild(title_text_box);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(author_label);
    edit_form.appendChild(fname_text_box);
    edit_form.appendChild(lname_text_box);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(isbn10_label);
    edit_form.appendChild(isbn10_text_box);

    edit_form.appendChild(document.createElement('br'));

    edit_form.appendChild(isbn13_label);
    edit_form.appendChild(isbn13_text_box);

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

    var editID = 'edit' + isbn10;

    //alert("editID: " + editID);
    document.getElementById(editID).style.display = "block";
    document.getElementById("container").style.height = "calc(100vh - 7em)";
    document.getElementById("container").style.overflow = "hidden";
}

function lendModal(book) {
    console.log(book);
}