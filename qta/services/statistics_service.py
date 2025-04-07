from .statistics_interface import IStatisticsService
from qta.models import Ticket
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import pandas as pd
import datetime

class StatisticsService(IStatisticsService):

    def generate_statistics(self):
        tickets = Ticket.objects.all()
        equipment_counts = {}

        for ticket in tickets:
            equipment_counts[ticket.equipment] = equipment_counts.get(ticket.equipment, 0) + 1

        max_equipment = max(equipment_counts.items(), key=lambda x: x[1], default=("None", 0))[0]

        # Histograma de prioridades
        df = pd.DataFrame([t.priority for t in tickets], columns=['priority'])
        priority_counts = df['priority'].value_counts()
        max_priority = priority_counts.idxmax() if not priority_counts.empty else "None"

        # Tarta de estados (última semana)
        df = pd.DataFrame(tickets.values('call_time', 'state'))
        now = datetime.datetime.now()
        week_ago = pd.to_datetime(now - datetime.timedelta(days=7), utc=True)
        recent_tickets = df[df['call_time'] >= week_ago]
        state_counts = recent_tickets['state'].value_counts()
        max_state = state_counts.idxmax() if not state_counts.empty else "None"

        # Lugar más frecuente (última semana)
        df = pd.DataFrame(tickets.values('call_time', 'place'))
        recent_places = df[df['call_time'] >= week_ago]['place'].value_counts()
        max_place = recent_places.idxmax() if not recent_places.empty else "None"

        # Gráficas
        plt.bar(equipment_counts.keys(), equipment_counts.values())
        plt.savefig("graph.jpg")
        plt.clf()

        priority_counts.plot(kind='bar')
        plt.savefig("graph2.jpg")
        plt.clf()

        if not state_counts.empty:
            plt.pie(state_counts, labels=state_counts.index, autopct='%1.1f%%')
            plt.savefig("graph4.jpg")
            plt.clf()

        if not recent_places.empty:
            plt.barh(recent_places.index, recent_places)
            plt.savefig("graph5.jpg")
            plt.clf()

        return {
            'Max_Equipment': max_equipment,
            'Max_Priority': max_priority,
            'Max_State': max_state,
            'Max_Place': max_place
        }
