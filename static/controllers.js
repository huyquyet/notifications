var NotiControllers = angular.module('NotiControllers', []);

NotiControllers.controller('NotiController', ['$scope', '$dragon', function ($scope, $dragon) {
    $scope.notiList = [];
    $scope.change = 'noti';

    $dragon.onReady(function () {
        $dragon.open(function () {
            $dragon.subscribe('notifications', $scope.change).then(function (response) {
                $scope.dataMapper = new DataMapper(response.data);

            });
        });
        $dragon.getList('notifications').then(function (response) {
            $scope.notiList = response.data;
        });
    });
    $dragon.onChannelMessage(function (channels, message) {
        if (indexOf.call(channels, $scope.channel) > -1) {
            $scope.$apply(function () {
                $scope.dataMapper.mapData($scope.notiList, message.data);
            });
        }
    })
}]);