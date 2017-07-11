"""Constants"""

COLUMNS = ['TEMP','MIN','MAX','DEWP',
                        'DIR','SPD','GUS','PCPXX',
                        'PCP06','PCP24','SD','SKC','CLG',
                        'L','M','H','SLP','STP',
                        'ALT','VSB']

FILE_NAME = 'weather-info.csv'
UPDATE_NULL_IF_ZERO = "UPDATE testone SET {0}=NULL WHERE {0}::varchar= '0'"
