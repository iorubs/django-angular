(function () {
    'use strict';

    angular
        .module('keeperoo.home', [
            'keeperoo.home.controllers',
            'keeperoo.home.services'
        ]);

    angular
        .module('keeperoo.home.controllers', []);

    angular
        .module('keeperoo.home.services', ['ngCookies']);
})();
