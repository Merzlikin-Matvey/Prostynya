const path = require('path');
const { createFiles } = require('./tasks');

module.exports = (req, res) => {
    const num = Number(req.body.num);
    const size = Number(req.body.size);
    const title = String(req.body.title);
    const fileName = String(req.body.fileName);

    createFiles(num, size, "Addition", title, fileName);

    const projectDirectory = path.join(__dirname, '..', '..');
    const filePath = path.join(projectDirectory, 'latex', fileName + ".pdf");

    res.setHeader('Content-Disposition', `attachment; filename="${fileName}.pdf"`);
    res.sendFile(filePath);
};
