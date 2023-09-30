const path = require("path");
const { createFile, generateID } = require("./tasks");

function getFileName(filePath) {
  return (fileName = path.basename(filePath));
}

const generateFile = (req, res) => {
  console.log(req.body);

  let num = Number(req.body.num);
  let size = Number(req.body.size);
  let operation = "Addition";
  let fileTitle = String(req.body.fileTitle);
  let fileName = String(req.body.fileName);
  let variants = 1;
  let writeID = true;

  if (!fileName || fileName == "undefined" || fileName == undefined) {
    fileName = generateID();
  }

  paths = createFile(num, size, operation, fileTitle, fileName);

  res.setHeader(
    "Content-Disposition",
    `attachment; filename="${fileName}.pdf"`
  );
  res.send(paths);
};

const downloadFile = (req, res) => {
  let filePath = req.body.filePath;
  let fileName = getFileName(filePath);
  res.setHeader(
    "Content-Disposition",
    `attachment; filename="${fileName}"`
  );
  res.sendFile(filePath);
};

module.exports = { generateFile, downloadFile };
