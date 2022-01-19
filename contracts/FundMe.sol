pragma solidity ^0.6.0;

import "@chainlink/contracts/src/v0.6/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.6/vendor/SafeMathChainlink.sol";


contract FundMe {
  using SafeMathChainlink for uint256;

  mapping(address => uint256) public cheese;
  address public owner;
  AggregatorV3Interface public priceFeed; 

  constructor(address _priceFeed) public {
    priceFeed = AggregatorV3Interface(_priceFeed);
    owner = msg.sender;
  } 


  function fund() public payable {
     uint256 minimumUSD = 50 * 10 ** 18;
     require(getConversionRate(msg.value) >= minimumUSD, "spend more Eth Dude");
     cheese[msg.sender] += msg.value; 
  }

  function getVerison() public view returns (uint256) {
    return priceFeed.version();
  }

  function getPrice() public view returns (uint256) {
     (,int256 answer,,,) = priceFeed.latestRoundData();
         // ETH/USD rate in 18 digit 
      return uint256(answer * 10000000000);
  }


  function getConversionRate(uint256 ethAmount) public view returns (uint256) {
    uint256 ethPrice = getPrice();
    uint256 ethAmountinUsd = (ethPrice * ethAmount) / 1000000000000000000;
    return ethAmountinUsd;
  }

  modifier onlyOwner {
    require(msg.sender == owner);
    _;
  }



  function withdraw() payable onlyOwner public {
    msg.sender.transfer(address(this).balance);
  }






}