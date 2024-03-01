import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud

from sorting import sort_dict_alphabetically, letter_count
letter_count_dict = sort_dict_alphabetically(letter_count)

#=================================#
# * Letter frequency – histogram
#=================================#
plt.style.use('_mpl-gallery')

x = 0.5 + np.arange(len(letter_count_dict))
y = list(letter_count_dict.values())

fig, ax = plt.subplots()

ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

ax.set_xticks(x)
ax.set_xticklabels(letter_count_dict.keys())

ax.set_xlabel("Letters")
ax.set_ylabel("Count")

fig.set_figwidth(8)
fig.set_figheight(6)
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

plt.show()


#==================================#
# * Letter frequency – word cloud
#==================================#
wordcloud = WordCloud(background_color="lightgrey", width=800, height=400)

wordcloud.generate_from_frequencies(letter_count_dict)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
