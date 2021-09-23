
var app = angular.module('myApp', ['ngRoute']);

app
    .config(function ($routeProvider, $locationProvider) {
        console.log('I started')
        $routeProvider
            .when('/Home', {
                templateUrl: 'Home'
            })
            .when('/Setup', {
                templateUrl: 'Setup'
            })
            .otherwise({ redirectTo: '/Home' })
        console.log('i didnt do good right')
        $locationProvider.html5Mode({
            enabled: true,
            requireBase: false
        });
    })
    .controller('MainCtrl', function ($scope, $http) {
        console.log('loads?')
        $scope.testme = function() {
            console.log('yeep')
            alert("123")
        }
    })