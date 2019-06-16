{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "def calc_age(uid):\n",
    "    \n",
    "    payload = {'v': '5.71',\n",
    "               'access_token': 'd64f6c47d64f6c47d64f6c478ad6244585dd64fd64f6c478b493253bdb3de2493d99e16', \n",
    "               'user_id': str(uid),\n",
    "               'fields': 'bdate'}\n",
    "    r = requests.get('https://api.vk.com/method/friends.get', params=payload)\n",
    "    python_obj = json.loads(r.text)\n",
    "    \n",
    "    cd = datetime.now().date()\n",
    "    list_ages = []\n",
    "    for element in python_obj['response']['items']:\n",
    "        try:\n",
    "            if element['bdate'].count('.') > 1: \n",
    "                bithday = datetime.strptime(element['bdate'], '%d.%m.%Y')\n",
    "                age = int((cd-bithday.date()).days/365)\n",
    "                list_ages.append(age)\n",
    "        except:\n",
    "            pass\n",
    "    dict(Counter(list_ages))\n",
    "    result = sorted(rt.items(), key=lambda x: -x[1])\n",
    "    return(result)\n",
    "    \n",
    "\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    res = calc_age('reigning')\n",
    "    print(res)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
