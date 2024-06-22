const Poker = artifacts.require("Poker");
const CardLib = artifacts.require("CardLib");
const PlayLib = artifacts.require("PlayLib");

module.exports = function(deployer) {
  deployer.deploy(CardLib);
  deployer.link(CardLib, PlayLib);
  deployer.deploy(PlayLib);
  deployer.link(CardLib, Poker);
  deployer.link(PlayLib, Poker);
  deployer.deploy(Poker);
};
