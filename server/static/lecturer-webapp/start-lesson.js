var myLatLng = {
  lat: 52.4074963,
  lng: -1.5047307
};

function myMap() {
  var mapOptions = {
    center: new google.maps.LatLng(myLatLng),
    zoom: 16,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  var map = new google.maps.Map(document.getElementById("start-map"), mapOptions);
  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Building',
  });
}


function nearestHour(date) {
  date.setHours(date.getHours() + Math.round(date.getMinutes() / 60));
  date.setMinutes(0);
  return date;
}


app.controller('StartLessonController', function ($scope, $http) {
  var now = new Date();
  now.setSeconds(0, 0);
  $scope.event = {
    'date': now,
    'time': {}
  };
  $scope.event.time.start = nearestHour(new Date(2018, 2, 27, 18, 00));
  $scope.event.time.end = nearestHour(new Date(2018, 2, 27, 20, 00));

  $scope.room = {
    "code": "",
    "buildings": "",
    "coords": []
  }

  function getRoomInfo(room) {
    $http({
      method: 'GET',
      url: '/api/get-room?room=' + room
    }).then(function successCallback(response) {
      if (response.data.data.building && response.data.data.building != "Unknown building") {
        $scope.room.building = response.data.data.building;
        document.getElementById("start-map").classList.remove('collapse');

        if (response.data.data.coordinates) {
          var newLatLng = myLatLng;
          if (newLatLng['lat'] != response.data.data.coordinates[0] && newLatLng['lng'] != response.data.data.coordinates[1]) {
            myLatLng = {
              'lat': response.data.data.coordinates[0],
              'lng': response.data.data.coordinates[1],
            }
            myMap();
          }
        }
      } else {
        $scope.room.building = "";
      }
    }, function errorCallback(response) {
      console.log('error');
    });
  }

  $scope.$watch('room.code', function () {
    if ($scope.room.code && $scope.room.code.length > 1) {
      getRoomInfo($scope.room.code);
    }
  });
});