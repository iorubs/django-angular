(function () {
    'use strict';

    angular
        .module('keeperoo.auth', [
            'keeperoo.auth.controllers',
            'keeperoo.auth.services'
        ]);

    angular
        .module('keeperoo.auth.controllers', []);

    angular
        .module('keeperoo.auth.services', ['ngCookies']);
})();
