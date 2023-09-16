const { generateSingleTask } = require('./tasks');

const redirect = (req, res) => {
    res.redirect('/gamePage');
}

function newTask(size){
    return (generateSingleTask(size, "Addition"))
}

module.exports = {
    redirect,
    newTask
}



