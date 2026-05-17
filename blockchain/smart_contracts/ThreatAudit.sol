// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract ThreatAudit {
    struct ThreatRecord {
        string eventHash;
        uint256 timestamp;
    }

    ThreatRecord[] public records;

    event ThreatLogged(
        string eventHash,
        uint256 timestamp
    );

    function logThreat(
        string memory _eventHash
    ) public {
        records.push(
            ThreatRecord(
                _eventHash,
                block.timestamp
            )
        );

        emit ThreatLogged(
            _eventHash,
            block.timestamp
        );
    }

    function getRecordCount()
        public
        view
        returns (uint256)
    {
        return records.length;
    }
}
