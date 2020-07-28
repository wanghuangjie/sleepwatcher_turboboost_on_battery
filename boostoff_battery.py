import os,re,subprocess,time


def main():
    '''The main entry.'''
    # Note: do not use single quote here, because Alfred doesn't give choice to
    # escape a single quote.
    os.chdir('/Applications/Utilities/voltageshift')
    time.sleep(5)
    #result = re.search('Turbo Boost (.*)',str(subprocess.run(['sudo','./voltageshift','turbo'], capture_output=True).stdout)).group(1)[2:-3]
    result = re.search('Connected: (...)',str(subprocess.run(['system_profiler','SPPowerDataType'], capture_output=True).stdout)).group(1)
    #print(result)
    if result != 'Yes':
        os.system('sudo ./voltageshift turbo 0 > /dev/null')
        os.system("osascript -e 'display notification \"Turboboost Disabled!\" with title \"On Battery\"'")
    else:
        #os.system('sudo ./voltageshift turbo 1 > /dev/null')
        pass
        print("we do nothing because it's on charging")


if __name__ == '__main__':
    main()