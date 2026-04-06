const express = require("express");
const app = express();

// Server 2 (PORT 3001) - Fast
app.get("/", (req, res) => {
  res.send("Fast Server - Port 3001");
});

app.listen(3001, () => {
  console.log("Fast server running on port 3001");
});
