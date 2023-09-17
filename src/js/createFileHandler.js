const path = require('path');
const { createFile } = require('./tasks');

function getFileName(filePath) {
    return fileName = path.basename(filePath)
  }

module.exports = (req, res) => {
        const num = Number(req.body.num);
        const size = Number(req.body.size);
        const operation = "Addition";
        const title = String(req.body.title);
        const fileName = String(req.body.fileName);
        const variants = 1;
        const writeID = true;

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





