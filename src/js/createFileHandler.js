const path = require('path');
const { createFile, generateID } = require('./tasks');

function getFileName(filePath) {
    return fileName = path.basename(filePath)
  }

const generateFile = (req, res) => {
        let num = Number(req.body.num);
        let size = Number(req.body.size);
        let operation = "Addition";
        let title = String(req.body.title);
        let fileName = String(req.body.fileName);
        let variants = 1;
        let writeID = true;

        if (!fileName || fileName == 'undefined' || fileName == undefined){
            fileName = generateID()
        }

        paths = createFile(
            num, 
            size, 
            operation, 
            title, 
            fileName
        );
        
        res.setHeader('Content-Disposition', `attachment; filename="${fileName}.pdf"`);
        res.sendFile(paths[0]);
}

module.exports = { generateFile }





