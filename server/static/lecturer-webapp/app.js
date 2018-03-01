var app = angular.module('cuasApp', ["ngRoute"]);

app.controller('DashboardController', function ($scope) {
  $scope.displayName = "Ada";
  $scope.greeting = "";

  var today = new Date()
  var curHr = today.getHours()

  if (curHr < 12) {
    $scope.greeting = 'Good morning';
  } else if (curHr < 18) {
    $scope.greeting = 'Good afternoon';
  } else {
    $scope.greeting = 'Good evening';
  }

  $scope.greeting += ', ' + $scope.displayName + '!';
});

app.config(function ($routeProvider) {
  $routeProvider
    .when("/", {
      templateUrl: "static/lecturer-webapp/dashboard.html"
    })
    .when("/test", {
      templateUrl: "static/lecturer-webapp/test.html"
    })
    .when("/start", {
      templateUrl: "static/lecturer-webapp/start-lesson.html"
    })
    .when("/lessons", {
      templateUrl: "static/lecturer-webapp/lessons.html"
    });
});