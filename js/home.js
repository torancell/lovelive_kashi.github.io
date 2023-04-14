const fs = require('fs');
const path = require('path');

const directoryPath = '../songlist/Aqours';
const files = [];

fs.readdir(directoryPath, function (err, fileNames) {
    if (err) {
        console.log('Unable to read directory: ' + err);
        return;
    }

    fileNames.forEach(function (fileName) {
        const filePath = path.join(directoryPath, fileName);
        files.push(filePath);
    });

    console.log(files);
});
