const express = require("express");
const cors = require("cors");
const { spawn } = require("child_process");

const app = express();
app.use(express.json());
app.use(cors());

app.post("/track", (req, res) => {
  const { url, target_price, email } = req.body;
  
  const pythonProcess = spawn("python3", ["tracker.py", url, target_price, email]);
  
  pythonProcess.stdout.on("data", (data) => {
    console.log(`Python Output: ${data}`);
  });

  pythonProcess.stderr.on("data", (data) => {
    console.error(`Error: ${data}`);
  });

  pythonProcess.on("close", (code) => {
    if (code === 0) {
      res.json({ message: "Tracking started successfully!" });
    } else {
      res.status(500).json({ message: "Failed to start tracking." });
    }
  });
});

app.listen(5000, () => {
  console.log("Server running on port 5000");
});

