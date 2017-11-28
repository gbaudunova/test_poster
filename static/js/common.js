const selected_portal = $('#id_name');
const messages = $('#messages');
const selected_portals = $('.selected_portals')
const sel_portal = document.getElementById('select_portal');
const name_inp = document.getElementById('id_name');
let list_portal_name = document.getElementById('portal_name');
let list_portals = document.getElementById('list_portals');

sel_portal.addEventListener('change', () => {
    name_inp.value = this.value;
}, false);

list_portals.addEventListener('click', (e) => {
    let target = e.target;
    if (target.getAttribute("id") == 'portal_name') {
        let a = target.innerHTML;
        c = $(selected_portals).children()
        if (c.length == 0) {
            $(selected_portals).append(
                `<input type="text" value="${a}" name="selected_portal">`
            );
        } else {
            // Dev!
            for (let i = 0; i < c.length; i++) {
                if ($(c[i]).val() == a) {
                    $(c[i]).remove();
                } 
                if ($(c[1]).val() != a) {
                    $(selected_portals).append(
                        `<input type="text" value="${a}" name="selected_portal">`
                    );
                }
            }
            // End Dev
        }
    }
}, false);

(function set_default_portal() {
    selected_portal.val(sel_portal[0].value)
})();

// Hide message after 4 seconds
(function hideMessage() {
    setTimeout(function () {
        messages.fadeOut('slow');
    }, 4000);
})();


$('.the_portal').click(function (event) {
    elem = $(this);
    $(elem).toggleClass('the_portal_disable');
    $(elem).children('span').toggleClass('lamp_disable');
});

