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
  var nearest = nearestHour(now);

  $scope.event = {
    'date': now,
    'time': {
      'startVal': ('0' + nearest.getHours()).slice(-2) + ':00',
      'endVal': ('0' + ((nearest.getHours() + 2) % 24)).slice(-2) + ':00'
    }
  };


  $scope.room = {
    "code": "",
    "buildings": "",
    "coords": []
  };


  $scope.submitForm = function () {
    var dateStr = $scope.event.date.toISOString().slice(0, 10) + " ";

    var formData = {
      'username': getCookie('cuas_lecturer_login_username'),
      'room': $scope.room.code,
      'start': dateStr + document.getElementById('startTime').value + ":00",
      'end': dateStr + document.getElementById('endTime').value + ":00"
    };

    // Backend call to start new lesson
    $http({
      method: 'POST',
      url: '/api/start-lesson',
      headers: {
        'Content-Type': 'application/json'
      },
      data: JSON.stringify(formData)
    }).then(function successCallback(response) {
      $scope.event.id = response.data.data.event_id;
      document.getElementById("qrCard").classList.remove('collapse');
      document.getElementById('start-button').setAttribute('disabled', 'true');

    }, function errorCallback(response) {
      alert('An error occured');
      console.log(response);
    });
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