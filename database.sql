-- Create the patients table
CREATE TABLE patients (
  id INT PRIMARY KEY AUTO_INCREMENT,
  name VARCHAR(100) NOT NULL,
  idNumber VARCHAR(20) NOT NULL,
  mobileNumber VARCHAR(20) NOT NULL,
  gender VARCHAR(10) NOT NULL,
  age INT NOT NULL,
  weight DECIMAL(5, 2) NOT NULL,
  height DECIMAL(5, 2) NOT NULL
);

-- Create the medical_records table
CREATE TABLE medical_records (
  id INT PRIMARY KEY AUTO_INCREMENT,
  patientId INT NOT NULL,
  date DATE NOT NULL,
  doctor VARCHAR(100) NOT NULL,
  details TEXT NOT NULL,
  FOREIGN KEY (patientId) REFERENCES patients(id)
);