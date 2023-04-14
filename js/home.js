const fs = require('fs');
const path = require('path');

const directoryPath = '../songlist/Aqours';

fs.readdir(directoryPath, function (err, files) {
    if (err) {
        console.log('Error getting directory information.');
    } else {
        let filePaths = [];
        files.forEach(function (file) {
            filePaths.push(path.join(directoryPath, file));
        });
        console.log(filePaths);
    }
});
