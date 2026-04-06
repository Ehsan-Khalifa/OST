const express = require("express");
const app = express();

// Server 1 (PORT 3000) - Slow
app.get("/", (req, res) => {
  setTimeout(() => {
    res.send("Slow Server - Port 3000");
  }, 5000);
});

app.listen(3000, () => {
  console.log("Slow server running on port 3000");
});
