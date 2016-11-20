(function () {
    'use strict';

    angular
        .module('keeperoo', [
            'keeperoo.config',
            'keeperoo.routes',
            'keeperoo.layout',
            'keeperoo.home',
            'keeperoo.auth',
        ])
        .run(run);

    run.$inject = ['$http'];

    function run($http) {
        $http.defaults.xsrfHeaderName = 'X-CSRFToken';
        $http.defaults.xsrfCookieName = 'csrftoken';
    }

    angular
        .module('keeperoo.config', []);

    angular
        .module('keeperoo.routes', ['ngRoute']);
})();
