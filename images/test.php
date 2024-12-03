<?php
$conn = new mysqli("sql303.infinityfree.com", "if0_37817887", "jNORZbVDH3", "if0_37817887_if0_37817887_ ");
$sql = "INSERT INTO Compte VALUES('Bob','Boby','boby.bob@gmail.com','azerty','azerty',100);";
if ($conn->query($sql)) {
    echo "value inserted";
} else {
    echo "insertion failed";
}

$sql = "SELECT * FROM Compte;";
if ($result->num_rows > 0) {
    echo "<table border=1>";
    echo "<tr><th>number</th><th>name</th></th>";
    while ($row = $result->fetch_assoc()) {
        echo "<tr><td>" . $row['id'] . "</td><td>" . $row['name'] . "</td></tr>";
    }
    echo "<table>";
} else {
    echo "0 row available";
}
$conn->close();
