const { generateSingleTask } = require("./tasks");

const redirectFiniteGame = (req, res) => {
  let size = req.body.size;
  let num = req.body.num;
  try{
    size = Number(size);
  }
  finally {
    size = 3;
  }

  try{
    num = Number(num);
  }
  finally {
    num = 5;
  }


  res.redirect(
    "/finiteGamePage" + "?size=" + size + "&num=" + num
  );
};

function newTask(size) {
  return generateSingleTask(size, "Addition");
}

module.exports = {
  redirectFiniteGame,
  newTask,
};
