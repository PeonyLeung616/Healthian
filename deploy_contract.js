var web3 = new Web3(Web3.givenProvider || "http://localhost:8545");

var contractAddress = "0x2472dB4f635D40E62c6012E2B390AFb4a062E4Fe";
var contractABI = [ /* Paste your contract's ABI here */ ];

var contract = new web3.eth.Contract(contractABI, contractAddress);


contract.methods.myFunction().call(function(error, result) {
    if (!error) {
      console.log(result);
    } else {
      console.error(error);
    }
  });

document.getElementById("result").textContent = result;