import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from uuid import uuid4

def load_and_clean_data(filepath):
    print("Đọc dữ liệu từ file:", filepath)
    df = pd.read_csv(filepath)
    cols_to_drop = ['email', 'extracurricular_activities', 'history_score', 'biology_score', 'geography_score']
    df = df.drop(columns=cols_to_drop)
    df['average_score'] = df[['math_score', 'physics_score', 'chemistry_score', 'english_score']].mean(axis=1)
    return df


def group_students(df):
    df_grouped = df.groupby(['id', 'first_name', 'last_name', 'gender'], as_index=False).agg({
        'math_score': 'mean',
        'physics_score': 'mean',
        'chemistry_score': 'mean',
        'english_score': 'mean',
        'average_score': 'mean'
    })
    print("\nThông tin điểm trung bình từng học sinh (5 bản ghi đầu):")
    print(df_grouped.head(5).to_string(index=False))
    return df_grouped


def classify_students(df):
    def xep_loai(score):
        if score > 80:
            return 'Giỏi'
        elif score > 65:
            return 'Khá'
        elif score > 50:
            return 'Trung bình'
        else:
            return 'Yếu'

    df['classification'] = df['average_score'].apply(xep_loai)
    print("\nThêm cột phân loại học lực (5 bản ghi đầu):")
    print(df[['id', 'first_name', 'average_score', 'classification']].head(5).to_string(index=False))
    return df


def count_by_classification(df):
    so_luong = df['classification'].value_counts()
    print("\nSố lượng học sinh theo phân loại học lực:")
    print(so_luong.to_string())


def summarize_study_hours(df):
    df['study_hours_bin'] = pd.cut(
        df['weekly_self_study_hours'],
        bins=[0, 10, 20, 30, 40, 50],
        labels=['0-10', '11-20', '21-30', '31-40', '41-50'],
        right=True
    )
    summary = df.groupby('study_hours_bin', observed=True).agg(
        average_score_mean=('average_score', 'mean'),
        student_count=('id', 'count')
    ).reset_index()
    print("\nTóm tắt số lượng và điểm trung bình theo nhóm giờ tự học:")
    print(summary.to_string(index=False))


def summarize_gender_classification(df):
    summary = df.groupby(['gender', 'classification'], observed=True).agg(
        avg_score=('average_score', 'mean'),
        count=('id', 'count')
    ).reset_index()
    print("\nTóm tắt điểm trung bình và số lượng học sinh theo giới tính và phân loại học lực:")
    print(summary.to_string(index=False))


def job_gender_stats(df):
    stats = df.groupby(['gender', 'part_time_job'], observed=True).agg(
        average_score_mean=('average_score', 'mean'),
        average_score_std=('average_score', 'std'),
        count=('average_score', 'size')
    ).reset_index()
    print("\nThống kê điểm trung bình, độ lệch chuẩn và số lượng theo giới tính và công việc part-time:")
    print(stats.to_string(index=False))


def classification_ratio_career(df):
    classification_stats = df.groupby(['career_aspiration', 'classification']).agg(
        count=('id', 'count'),
        min_avg_score=('average_score', 'min'),
        max_avg_score=('average_score', 'max')
    ).reset_index()

    total_by_career = classification_stats.groupby('career_aspiration')['count'].transform('sum')
    classification_stats['percentage'] = (classification_stats['count'] / total_by_career * 100).round(2)

    classification_stats = classification_stats.sort_values(['career_aspiration', 'classification'])

    print("\n📊 Tỉ lệ học sinh theo học lực trong từng nguyện vọng nghề nghiệp (kèm điểm trung bình cao/thấp):")
    print(classification_stats.to_string(index=False))


def pivot_career_rank(df):
    pivot = pd.pivot_table(
        df,
        index='career_aspiration',
        values='average_score',
        aggfunc='mean'
    )
    pivot['rank'] = pivot['average_score'].rank(ascending=False, method='dense').astype(int)
    pivot = pivot.sort_values('rank')
    pivot['average_score'] = pivot['average_score'].round(2)
    print("\nXếp hạng điểm trung bình các ngành học (dùng pivot_table):")
    print(pivot.reset_index().to_string(index=False))


def top_student_by_career(df):
    top_students = df.groupby('career_aspiration').apply(
        lambda group: group[group['average_score'] == group['average_score'].max()]
    ).reset_index(drop=True)

    print("\n🏆 Học sinh có điểm trung bình cao nhất trong từng ngành nghề:")
    print(top_students[['career_aspiration', 'first_name', 'last_name', 'average_score']].to_string(index=False))
#
def pivot_classification_gender(df):
    pivot = pd.pivot_table(
        df,
        index='classification',
        columns='gender',
        values='average_score',
        aggfunc='mean'
    ).round(2).reset_index()
    print("\nĐiểm trung bình theo phân loại học lực và giới tính (dùng pivot_table):")
    print(pivot.to_string(index=False))


def top_student_by_career(df):
    results = []
    for career, group in df.groupby('career_aspiration'):
        top_score = group['average_score'].max()
        top_students = group[group['average_score'] == top_score]
        results.append(top_students)
    top_students_df = pd.concat(results).reset_index(drop=True)

    print("\n🏆 Học sinh có điểm trung bình cao nhất trong từng ngành nghề:")
    print(top_students_df[['career_aspiration', 'first_name', 'last_name', 'average_score']].to_string(index=False))



# Hàm chuẩn hoá Z-score

def zscore(series):
    return (series - series.mean()) / series.std()


def add_zscore_and_study_diff(df):
    df['zscore_by_gender'] = df.groupby('gender')['average_score'].transform(zscore)

    def pct_diff(series):
        return ((series - series.mean()) / series.mean()) * 100

    df['study_hours_pct_diff'] = df.groupby('career_aspiration')['weekly_self_study_hours'].transform(pct_diff)

    print("\nThêm cột Z-score và phần trăm lệch giờ học:")
    print(df[['first_name', 'gender', 'zscore_by_gender', 'career_aspiration', 'study_hours_pct_diff']].head().to_string(index=False))
    #
    # Thêm 1 transform khác: Tính khoảng cách điểm số so với trung bình theo từng học lực
    df['score_gap_by_classification'] = df['average_score'] - df.groupby('classification')['average_score'].transform(
        'mean')

    print("\n📌 Thêm cột Z-score, phần trăm lệch giờ học, và khoảng cách điểm trung bình so với nhóm học lực:")
    print(df[['first_name', 'gender', 'zscore_by_gender', 'career_aspiration', 'study_hours_pct_diff', 'classification',
              'score_gap_by_classification']].head().to_string(index=False))


def plot_subject_means(df):
    # Tự động phát hiện các cột có "_score"
    subject_columns = [col for col in df.columns if col.endswith('_score')]

    if not subject_columns:
        print("Không có cột điểm nào để hiển thị.")
        return

    # Tính điểm trung bình các môn học
    subject_means = df[subject_columns].mean().sort_values(ascending=False)

    # Làm đẹp tên hiển thị
    subjects = [subject.replace('_score', '').capitalize() for subject in subject_means.index]

    # In bảng điểm trung bình
    print("\n🎓 Điểm trung bình theo môn học:")
    print(subject_means.round(2).to_string())

    # Thiết lập giao diện seaborn
    sns.set_theme(style="whitegrid", font="Arial", font_scale=1.2)
    plt.figure(figsize=(14, 7), dpi=120)

    # Tạo palette màu gradient
    palette = sns.color_palette("Blues", n_colors=len(subjects))

    # Vẽ biểu đồ đường với hiệu ứng
    sns.lineplot(
        x=subjects,
        y=subject_means.values,
        marker='o',
        linewidth=4,
        markersize=12,
        palette=palette,
        markeredgecolor='black',
        markeredgewidth=1.5,
        zorder=2
    )

    # Trang trí biểu đồ
    plt.title('📈 Điểm trung bình theo môn học', fontsize=20, fontweight='bold', pad=20)
    plt.xlabel('Môn học', fontsize=16, labelpad=10)
    plt.ylabel('Điểm trung bình', fontsize=16, labelpad=10)
    plt.xticks(rotation=30, ha='right', fontsize=14)
    plt.yticks(fontsize=14)

    # Tùy chỉnh giới hạn trục y linh hoạt
    max_score = subject_means.max()
    plt.ylim(0, max_score + 10)  # Thêm khoảng trống cho text

    # Thêm chú thích điểm số
    for x, y in zip(subjects, subject_means.values):
        plt.text(
            x, y + 1, f"{y:.1f}",
            ha='center', va='bottom',
            fontsize=12, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.8, edgecolor='none', pad=1)
        )

    # Tùy chỉnh grid
    plt.grid(True, linestyle='--', alpha=0.5, zorder=1)
    sns.despine(left=True, bottom=True)  # Loại bỏ viền thừa

    # Tối ưu layout
    plt.tight_layout()

    # Lưu biểu đồ
    output_file = f"subject_means_plot_{uuid4().hex[:8]}.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"\n✅ Biểu đồ đã được lưu thành: {output_file}")

    # Hiển thị biểu đồ
    plt.show()


def main():
    filepath = "D:\data_python/student-scores.csv"
    df = load_and_clean_data(filepath)
    group_students(df)
    df = classify_students(df)
    count_by_classification(df)
    summarize_study_hours(df)
    summarize_gender_classification(df)
    job_gender_stats(df)
    classification_ratio_career(df)
    add_zscore_and_study_diff(df)
    pivot_career_rank(df)
    pivot_classification_gender(df)
    top_student_by_career(df)
    plot_subject_means(df)


if __name__ == "__main__":
    main()