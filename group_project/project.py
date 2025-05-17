import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu từ file CSV
df = pd.read_csv('D:\data_python/student-scores.csv')

print(df)
# Tiền xử lý dữ liệu
# Kiểm tra dữ liệu thiếu
print(df.info())  # Không có giá trị thiếu
# Tạo cột điểm trung bình
df['average_score'] = df[['math_score', 'history_score', 'physics_score', 
                         'chemistry_score', 'biology_score', 'english_score', 
                         'geography_score']].mean(axis=1)

print("Điểm trung bình:\n", df['average_score'].head())
# 1. Phân nhóm: Điểm trung bình theo giới tính và tham vọng nghề nghiệp
avg_score_by_gender_career = df.groupby(['gender', 'career_aspiration'])['average_score'].mean().reset_index()

print(avg_score_by_gender_career)


# 2. Pivot Table: Điểm trung bình các môn theo giới tính và tham vọng nghề nghiệp
pivot_table = pd.pivot_table(df, 
                            values=['math_score', 'history_score', 'physics_score', 
                                    'chemistry_score', 'biology_score', 'english_score', 
                                    'geography_score'],
                            index='gender',
                            columns='career_aspiration',
                            aggfunc='mean')

# 3. Apply: Tính tỷ lệ điểm trung bình của từng học sinh so với nhóm theo tham vọng nghề nghiệp
def calc_score_ratio(group):
    return group['average_score'] / group['average_score'].mean()

# Sửa cảnh báo DeprecationWarning bằng cách thêm include_groups=False
df['score_ratio'] = df.groupby('career_aspiration').apply(calc_score_ratio, include_groups=False).reset_index(drop=True)

# 4. Transform: Chuẩn hóa điểm số (z-score) theo giới tính cho từng môn
score_columns = ['math_score', 'history_score', 'physics_score', 
                 'chemistry_score', 'biology_score', 'english_score', 
                 'geography_score']
for col in score_columns:
    df[f'{col}_zscore'] = df.groupby('gender')[col].transform(lambda x: (x - x.mean()) / x.std())

# 5. Phân tích mối quan hệ giữa số giờ tự học và điểm trung bình
# Nhóm theo số giờ tự học (chia thành các khoảng)
df['study_hours_bin'] = pd.cut(df['weekly_self_study_hours'], bins=[0, 10, 20, 30, 40, 50], 
                              labels=['0-10', '11-20', '21-30', '31-40', '41-50'])

# Sửa cảnh báo FutureWarning bằng cách thêm observed=True
avg_score_by_study_hours = df.groupby('study_hours_bin', observed=True)['average_score'].mean().reset_index()

# 6. Pivot Table: Ảnh hưởng của ngày vắng học và hoạt động ngoại khóa đến điểm trung bình
pivot_absence_extracurricular = pd.pivot_table(df, 
                                             values='average_score',
                                             index='absence_days',
                                             columns='extracurricular_activities',
                                             aggfunc='mean')

# Trực quan hóa
# Biểu đồ 1: Điểm trung bình theo giới tính và tham vọng nghề nghiệp
plt.figure(figsize=(12, 6))
sns.barplot(data=avg_score_by_gender_career, x='career_aspiration', y='average_score', hue='gender')
plt.title('Điểm trung bình theo giới tính và tham vọng nghề nghiệp')
plt.xticks(rotation=45)
plt.savefig('avg_score_by_gender_career.png')
plt.close()

# Biểu đồ 2: Điểm trung bình theo số giờ tự học
plt.figure(figsize=(10, 6))
sns.barplot(data=avg_score_by_study_hours, x='study_hours_bin', y='average_score')
plt.title('Điểm trung bình theo số giờ tự học hàng tuần')
plt.xlabel('Số giờ tự học (giờ/tuần)')
plt.ylabel('Điểm trung bình')
plt.savefig('avg_score_by_study_hours.png')
plt.close()

# Biểu đồ 3: Heatmap cho pivot table (ngày vắng học và hoạt động ngoại khóa)
plt.figure(figsize=(10, 6))
sns.heatmap(pivot_absence_extracurricular, annot=True, cmap='YlGnBu', fmt='.1f')
plt.title('Điểm trung bình theo ngày vắng học và hoạt động ngoại khóa')
plt.xlabel('Hoạt động ngoại khóa')
plt.ylabel('Ngày vắng học')
plt.savefig('pivot_absence_extracurricular.png')
plt.close()

# Lưu kết quả phân tích
avg_score_by_gender_career.to_csv('avg_score_by_gender_career.csv', index=False)
pivot_table.to_csv('pivot_table_scores.csv')
pivot_absence_extracurricular.to_csv('pivot_absence_extracurricular.csv')

# Vẽ đường phân phối cho tất cả các môn trên cùng một đồ thị
for subject in score_columns:
    sns.kdeplot(data=df[subject], label=subject.replace('_score', '').capitalize())

plt.title('So sánh phân phối điểm các môn học')
plt.xlabel('Điểm số')
plt.ylabel('Mật độ')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('subject_score_comparison.png')
plt.close()

# [Rest of the previous code remains the same]


subject_columns = ['math_score', 'history_score', 'physics_score', 
                  'chemistry_score', 'biology_score', 'english_score', 
                  'geography_score']

# Tạo Series điểm trung bình với index là tên môn học
subject_means = df[subject_columns].mean()
# Đổi tên index để hiển thị đẹp hơn
subject_means.index = [subject.replace('_score', '').capitalize() for subject in subject_means.index]

print("\nĐiểm trung bình theo môn học:")
print(subject_means)

# Vẽ biểu đồ đường điểm trung bình theo môn
plt.figure(figsize=(12, 6))
subject_means.plot(kind='line', marker='o', linewidth=2, markersize=10)