STEP-1=> the script send.py
       
       =>import psutil as p                                                //import psutil library
        from riemann_client.transport import TCPTransport                                                       
        from riemann_client.client import QueuedClient                                              
        with QueuedClient(TCPTransport("192.168.43.173", 5555)) as client:                                       
                                                                            => The above code The QueuedClient class modifies the event
                                                                             method to add events to a queue instead of immediately sending them

        c = p.cpu_times()
        d = c.user
        client.event(service="CPU_Times", metric_f=d,ttl=120)  // Some of the libraries present in psutil were used such as cpu_times,cpu_count,cpu_stats
                                                               // cpu_freq and virtual_memory was used. and ttl is set to 120 seconds. where they would be shown for 120 seconds       
                                                               // where they would be displayed for 120 seconds 
        e = p.cpu_times()
        f = e.idle
        client.event(service="idle", metric_f=f,ttl=120)

        g = p.cpu_times()
        h = g.iowait
        client.event(service="idle", metric_f=h,ttl=120) 

        i = p.cpu_count()
        client.event(service="CPUCount", metric_f=i,ttl=120)

        j = p.cpu_stats()
        k = j.interrupts
        client.event(service="Interrupts", metric_f=k,ttl=120)

        l = p.cpu_stats()
        m = l.syscalls
        client.event(service="Systemcalls", metric_f=m,ttl=120)

        n = p.cpu_freq()
        o = n.current
        client.event(service="Current freq", metric_f=o,ttl=120)

        pp = p.cpu_freq()
        q = pp.min
        client.event(service="Min", metric_f=q,ttl=120)

        r = p.virtual_memory()
        s = r.total
        client.event(service="Total Memory", metric_f=s,ttl=120) 

        t = p.virtual_memory() 
        u = t.available
        client.event(service="available", metric_f=u,ttl=120)

        v = p.virtual_memory()
        w = v.used
        client.event(service="Used", metric_f=w,ttl=120) 


        client.flush()                                     //flush() method to send the current event queue as a single message
