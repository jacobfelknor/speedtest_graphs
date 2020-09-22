from django.core.management.base import BaseCommand
import speedtest


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        print("running speedtest...")
        st = speedtest.Speedtest()
        st.download()
        st.upload()
        st.get_best_server()
        results = st.results.dict()

        print(results)
