import pandas as pd

class Manager:
    '''
        A class that helps manage the data present in our trips dataset
    '''
    @staticmethod
    def getTransportTypeFromCompany(companyId, providers):
        '''
            returns the transport type of the company
        '''
        transport_type = ''
        company = providers[providers['id']==companyId]
        print('_____', companyId)
        if len(company)>0:
            company = company.iloc[0]
            transport_type = company['transport_type'] if not pd.isna(company['transport_type']) else ''
        return transport_type
    
    @staticmethod
    def transportTypesOfTicket(ticketId, tickets, providers):
        '''
            returns the transport types of the trip\n
            params :\n
                ticketId : ticket id of the trip\n
                tickets : tickets dataset
        '''
        companies = ''
        ticket = tickets[tickets['id']==ticketId]
        if len(ticket)>0:
            ticket = ticket.iloc[0]
            company = ticket['company'] if not pd.isna(ticket['company']) else ''
            other_companies = ticket['other_companies'] if not pd.isna(ticket['other_companies']) else ''
            companies = str(company) + ',' + str(other_companies)
        companies = companies.replace('{', '').replace('}', '')
        companies = companies.split(',')
        companies = list(filter(None, companies))
        companies = pd.unique(companies)
        companies = [int(c) for c in companies]
        transport_type = [Manager.getTransportTypeFromCompany(companyId, providers) for companyId in companies]
        transport_type = pd.unique(transport_type)
        return transport_type
