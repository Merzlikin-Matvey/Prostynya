const exec = require('child_process')
const fs = require('fs')
const path = require('path')

const projectDirectory = path.join(__dirname, '..', '..');

function getRandomNumber(size = 3) {
  return Math.floor(Math.random() * (10 ** size - 10 ** (size - 1)) + 10 ** (size - 1))
}

function generateSingleTask(size = 3, operation = "Addition") {
  let a = getRandomNumber(size)
  let b = getRandomNumber(size)
  return [a.toString() + "+" + b.toString(), a+b]
}

function createFiles(
  num, 
  size, 
  operation, 
  title,
  fileName) 
{
  const path = projectDirectory + '\\latex'

  let taskPath = path + "\\" + fileName + ".tex"
  let solutionPath = path + "\\solution.tex"

  let preamble = "" +
  "\\documentclass{article} \n" + 
  "\\usepackage[paperheight=297mm, paperwidth=210mm, top=20mm, bottom=20mm, left=20mm, right=20mm]{geometry} \n" +
  "\\usepackage{multicol} \n" +
  "\\usepackage[fontsize=15pt]{fontsize} \n" +
  "\\usepackage[russian]{babel} \n" +
  "\n" +
  "\\pagestyle{empty} \n" +
  "\\begin{document} \n" 

  let taskContent = preamble + 
  "\\begin{center} \n" +
  "   \\large{\\textit{" + title +"}} \n" +
  "\\end{center}" +
  "\\begin{multicols}{2}\n"

  let solutionContent = preamble +
  "\\begin{center} \n" +
  "   \\large{\\textit{" + title + " - решение" + "}} \n" +
  "\\end{center}" +
  "\\begin{multicols}{2}\n"


   for (let i = 1; i < num + 1; i++){
    let [task, solution] = generateSingleTask(size=size, operation=operation)

    taskContent += i.toString() + ")" + "$" +
       "\\,".repeat(1 + 2*(Math.floor(Math.log10(num + 1)) - Math.floor(Math.log10(i)))) +
       task + "$ \\par \n" 

    solutionContent += i.toString() + ")" + "$" +
      "\\,".repeat(1 + 2*(Math.floor(Math.log10(num + 1)) - Math.floor(Math.log10(i)))) +
      solution.toString() + "$ \\par \n" 
   }

  taskContent += "\\end{multicols} \n"
  taskContent += "\\end{document}"

  solutionContent += "\\end{multicols} \n"
  solutionContent += "\\end{document}"

  fs.writeFileSync(taskPath, taskContent)
  fs.writeFileSync(solutionPath, solutionContent)

  const taskCommand = `pdflatex -output-directory=${path} ${taskPath}`
  const solutionCommand = `pdflatex -output-directory=${path} ${solutionPath}`

  exec.execSync(taskCommand)
  exec.execSync(solutionCommand)
}

module.exports = { createFiles, generateSingleTask };

