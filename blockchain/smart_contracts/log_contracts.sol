pragma solidity ^0.8.0;

contract SecurityLogs {

    string public log;

    function setLog(string memory _log) public {
        log = _log;
    }
}
